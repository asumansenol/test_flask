import pytest
from flask import Flask
from main import app
from bs4 import BeautifulSoup
import random
from db import check_user_status
import time

# Create random name and email address
num = random.random()
name = 'test' + str(num)
email = 'test' + str(num) + '@gmail.com'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_should_return_form_with_email_name_fields(client):
    """Make sure the form page contains the name and email fields."""
    response = client.get('/form')
    data = response.data.decode()
    soup = BeautifulSoup(response.data, 'html.parser')
    # Check if page contains a form with the name and email fields
    assert soup.find('form')
    assert soup.find('input', {'name': 'name'})
    assert soup.find('input', {'name': 'email'})


def test_should_return_thank_you_page(client):
    """Make sure the thank you page is displayed after the form is submitted and the user is added to the database with status 'Received'."""
    response = client.post('/form', data={'name': name, 'email': email})
    data = response.data.decode()
    soup = BeautifulSoup(response.data, 'html.parser')
    # Check if page contains a thank you message
    assert soup.find('h1').text == 'Thank You for Your Request'
    with app.app_context():
        status = check_user_status(email, name)
        assert status == 'Received'


def test_should_return_status_completed_15_secs_later():
    """Make sure the status is updated to 'Completed' 15 seconds after the request is submitted."""
    with app.app_context():
        time.sleep(25)
        status = check_user_status(email, name)
        assert status == 'Completed'

def test_should_return_completed_page_for_the_same_user(client):
    """Make sure the completed page is displayed for the same user if the request is submitted again."""
    response = client.get('/form')
    response = client.post('/form', data={'name': name, 'email': email})
    data = response.data.decode()
    soup = BeautifulSoup(response.data, 'html.parser')
    # Check if page contains a completed message
    assert soup.find('h1').text == 'Your request has been completed'