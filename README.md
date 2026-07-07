Baldi Cosimo 7139980

Full-Stack Web Application
Django

---

# Project Description

This project is a web application developed with Django that allows organizers to create and manage events 
while attendees can browse available events and register for them.

The application implements role-based access control, ensuring that organizers and attendees have access only 
to the features intended for their role.

---

# Implemented Features

## Organizer
- Register and log in
- Create new events
- Edit own events
- Delete own events
- View the list of registered attendees
  
## Attendee
- Register and log in
- Browse all available events
- View event details
- Register for an event
- Cancel an existing registration

## General Features
- User authentication
- Role-based authorization
- Django Admin panel
- Responsive interface built with Bootstrap 5
- SQLite database with demo data

---

# Local Installation

1. Clone the repository
   
git clone https://github.com/cosimobaldi-unifi/ppm-backend
cd django_project

2. Create a virtual environment

Linux/macOS

python -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate

3. Install the required packages

pip install -r requirements.txt

4. Apply migrations
   
python manage.py migrate

5. Start the development server

python manage.py runserver

Open your browser at http://127.0.0.1:8000/


# SQLite Database

The repository includes the following SQLite database:

db.sqlite3

The database is already populated with demo users, demo events and registrations, allowing the application 
to be explored immediately after cloning the repository.

---

# Demo Accounts (Role: username password)

Admin: admin admin12345
Organizer: organizer ppm12345
Attendee: attendee attendeeppm 

---

# Online Deployment

Deployment URL: https://baldi-ppm-backend.onrender.com/
