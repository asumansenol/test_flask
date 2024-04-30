from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import threading
import time
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), default='')

# Create a PUT endpoint to update data
@app.route('/data/<key>', methods=['PUT'])
def update_data(request_id):
    if request.method == 'PUT':
        time.sleep(2)
        # Render the completed.html template directly
    with app.app_context():
        # Updating request status when the service is completed
        request = Request.query.get(request_id)
        request.status = 'Completed'
        db.session.commit()

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Check if the request already exists
        existing_request = Request.query.filter_by(name=name, email=email).first()
        if existing_request:
            if existing_request.status == 'Completed':
                return render_template('completed.html')
            else:
                return render_template('pending.html')

        new_request = Request(name=name, email=email)
        new_request.status = 'Received'
        db.session.add(new_request)
        db.session.commit()

        # HTTP PUT call to update the data using the update_data endpoint without using url
        threading.Thread(target=long_running_service, args=(new_request.id,)).start()
        # url = f'http://localhost:5000/update_data/{new_request.id}'
        # requests.put(url)

        # Start a new thread to handle the call to update_data
        # threading.Thread(target=long_running_service, args=(new_request.id,)).start()

        return render_template('thank_you.html')
    return render_template('form.html')

# PUT endpoint to update data
@app.route('/update_data/<key>', methods=['PUT'])
def long_running_service(key):
    # Render the completed.html template directly
    with app.app_context():
        time.sleep(2)
        # Updating request status when the service is completed

        request = Request.query.get(key)
        request.status = 'Completed'
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
