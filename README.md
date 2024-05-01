# Flask Web App

This app presenting a simple web page with a form that allows a user to enter their name and email address and submit the form. 
The app also interacts with a backend API when users submit the form.
With this task I have used Flask as a backend also I have used HTML for the frontend.
I have used MySQL as a database and I have deployed the application on Google Cloud Platform.

Application is available on Google Cloud Platform. You can access it via this link: https://web-app-dot-notional-device-421909-a8.lm.r.appspot.com/form
PUT endpoint is available on this link: https://another-service-dot-notional-device-421909-a8.lm.r.appspot.com/{key}, it should be called with the id of the user that needs to be updated.


In this application I have used the following technologies:
- Flask
- HTML
- Google Cloud Platform
- MySQL on Google Cloud Platform

## How to run the application
1. Clone the repository
2. Install the required libraries by running the following command:
```
pip install -r requirements.txt
```
3. Run the following command to start the application:
```
python main.py
```
4. Open the browser and go to the following link: http://127.0.0.1:8080/form

## How to deploy the application on Google Cloud Platform
1. Create a new project on Google Cloud Platform
2. Create a new MySQL instance on Google Cloud Platform
3. Create a new database on the MySQL instance
4. Add firewall rules to allow the application to connect to the MySQL instance, I have used this: 
```
0.0.0.0/0
```
5. Add the database credentials to the db.py file
6. Create a new App Engine application on Google Cloud Platform
7. Deploy the application by running the following command:
```
gcloud app deploy
```
8. Open the browser and go to the following link: https://web-app-dot-notional-device-421909-a8.lm.r.appspot.com/form
9. PUT endpoint is available on this link: https://another-service-dot-notional-device-421909-a8.lm.r.appspot.com/{key}, it should be called with the id of the user that needs to be updated.
10. I have stream logs from the command line by running the following command:
```
gcloud app logs tail -s web-app
```

## How to test the application
1. Run the following command to start the application:
```
pytest-3
```
2. The test will run and you will see the results in the terminal
3. Test cases cover the following:
- Test the form and validates whether email and name exist
- Test form submit and check if the user is added to the database with the status 'Received'
- Test the PUT endpoint and check if the user status is updated to 'Completed'
- Test adding the same user again and check if the page displays the message 'Your request has been completed'

