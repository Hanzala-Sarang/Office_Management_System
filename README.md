# Office Management System (Django)

## Introduction
The Office Management System is a Django-based web application that allows you to manage employee details in an office environment. It provides basic operations like viewing employee details, adding new employees, removing employees, and filtering employee information.

## Features
- View a list of all employees in the system.
- Add new employees with their details.
- Remove employees from the system.
- Filter and search for employee details based on various criteria.

## Prerequisites
Before you can run this project, make sure you have the following prerequisites installed:

Django version 4.2.5
python version 3.10.11

## Getting Started
Follow these steps to get your Office Management System up and running:

1. Clone the repository to your local machine:

2. Navigate to the project directory:

3. Create a virtual environment and activate it (optional but recommended):

4. Install the project dependencies:
command : pip install -r requirements.txt

5. Apply database migrations:
command : python manage.py makemigrations
          python manage.py migrate

6. Create a superuser account to manage the system:
command : python manage.py createsuperuser

7. Run the development server:
command : python manage.py runserver

8. Access the application in your web browser at `http://localhost:8000/`

