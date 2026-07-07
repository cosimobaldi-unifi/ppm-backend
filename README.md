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

# Browser Testing Scenario

## Organizer

1. Log in using the organizer account.
2. Navigate to the home page.
3. Click **Create New Event**.
4. Fill in the event form and save it.
5. Verify that the new event appears in the event list.
6. Open the event details page.
7. Edit the event and verify that the changes are saved.
8. Delete the event and verify that it is removed from the list.
9. Verify that only events created by the organizer can be edited or deleted.

## Attendee

1. Log in using the attendee account.
2. Browse the list of available events.
3. Open an event details page.
4. Click **Register to Event**.
5. Verify that the registration is shown in the attendees list.

## Permission Testing

- An attendee cannot create, edit or delete events.
- An organizer can only edit and delete events that they created.
- Only authenticated users can register for events.
