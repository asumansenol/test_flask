# Flask Web App

This is a simple web application that allows a user to submit a form with their name and email address. The application saves the user's name and email address to a database with a status of "Received". The application then displays a message to the user saying "Thank You for Your Request". The application then calls a backend API with the user's name and email address to update the status to "Completed". The application shows a message to the user saying "Your request has been completed" when the user submits the form again with the same name and email address.

Application is available on Google Cloud Platform. You can access it via this link: https://web-app-dot-notional-device-421909-a8.lm.r.appspot.com/form.
PUT endpoint is available on this link: https://another-service-dot-notional-device-421909-a8.lm.r.appspot.com/{key}, it should be called with the id of the user that needs to be updated.

## Functionality
1. User submit the form with their name and email address.
2. The app saves the user's name and email address to a database, with a status of "Received".
3. The app displays a message to the user saying "Thank You for Your Request".
4. When user submit the form, the app calls a backend API with the user's name and email address to update the status to "Completed", it takes 15 seconds to complete.
5. The app shows a message to the user saying "Your request has been completed" when user submit the form again with the same name and email address.

## Technologies
In this application I have used the following technologies:
- Flask
- HTML
- MySQL on Google Cloud Platform
- Google Cloud Platform App Engine

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
5. Create a new App Engine application on Google Cloud Platform
6. Deploy the application by running the following command:
```
gcloud app deploy
```
7. Open the browser and go to the following link: https://web-app-dot-notional-device-421909-a8.lm.r.appspot.com/form
8. PUT endpoint is available on this link: https://another-service-dot-notional-device-421909-a8.lm.r.appspot.com/{key}, it should be called with the id of the user that needs to be updated.
9. To stream logs from the command line run the following command:
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
- Test the form and validates whether email and name fields exist (Functionality 1).
- Test form submit and check if the user is added to the database with the status 'Received' and after the submission the page shows 'Thank You for Your Request' message (Functionality 2, 3).
- Test the PUT endpoint and check if the user status is updated to 'Completed' (Functionality 4).
- Test adding the same user again and check if the page displays the message 'Your request has been completed' (Functionality 5).

## Some notes
- The application doesn't validates the email address, it just checks if the email address and name are not empty, achieved by adding 'required' attribute to the input fields.
- The application only adds the user to the database if the user doesn't exist, achieved by checking if the user's name and email address already exist in the database. If the user exists, the application doesn't add the user to the database and shows the message 'Your request has been completed'.
- All the required validations can be added to the application, but I have kept it simple for the purpose of this task.