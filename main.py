from flask import Flask, render_template, request
import threading
import time
import requests
from db import add_user, check_user_exist, update_user_status

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Check if the request already exists
        existing_request = check_user_exist(name, email)
        if existing_request:
            if existing_request['Status'] == 'Completed':
                return render_template('completed.html')
            else:
                return render_template('pending.html')

        user_id = add_user({"name": name, "email": email, "status": "Received"})

        # HTTP PUT call to update the data using the update_data endpoint without using url
        # threading.Thread(target=long_running_service, args=(user_id,)).start()
        # url = f'https://notional-device-421909-a8.lm.r.appspot.com/update_data/{user_id}'
        # requests.put(url)

        # Start a new thread to handle the call to update_data
        threading.Thread(target=invoke_service, args=(user_id,)).start()

        return render_template('thank_you.html')
    return render_template('form.html')

def invoke_service(key):
    url = f'https://notional-device-421909-a8.lm.r.appspot.com/update_data/{key}'
    requests.put(url)

# PUT endpoint to update data
@app.route('/update_data/<key>', methods=['PUT'])
def long_running_service(key):
    # Render the completed.html template directly
    with app.app_context():
        time.sleep(15)
        # Updating request status when the service is completed

        update_user_status(key, 'Completed')
        return render_template('completed.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(host="0.0.0.0", port=8080)
