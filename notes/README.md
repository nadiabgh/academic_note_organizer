# Notanizer - Academic Notes Organizer

## About The Project

Notanizer is a web-based academic note organizer developed using Django.The application enables students to organize their courses and notes in a structured environment while providing a clean user interface.
The application allows authenticated users to create courses, manage notes, attach images and files, and search through their academic content efficiently.
Notanizer aims to simplify the process of managing academic content.

---

## Features

- User Authentication (Sign Up, Login, Logout)
- Course Management (Create, Edit, Delete)
- Note Management (Create, Edit, Delete)
- Image Upload
- File Upload
- Search Courses and Notes by Title
- Tree-Style Sidebar Navigation
- Responsive User Interface
- PostgreSQL Database
- Docker Support
- Unit Testing

---

## Database Models

### User

The application uses a custom user model that extends Django's built-in AbstractUser.

| Field | Type |
|--------|------|
| username | CharField |
| password | CharField |
| first_name | CharField |
| last_name | CharField |
| email | EmailField |

---

### Course

Stores course information created by each authenticated user.

| Field | Type | Description |
|--------|------|-------------|
| title | CharField | Course title |
| description | TextField | Optional course description |
| author | ForeignKey(User) | Owner of the course |
| created | DateTimeField | Creation date |

---

### Note

Stores notes that belong to a specific course.

| Field | Type | Description |
|--------|------|-------------|
| title | CharField | Note title |
| description | TextField | Optional description |
| content | TextField | Note content |
| course | ForeignKey(Course) | Related course |
| image | ImageField | Uploaded image |
| file | FileField | Uploaded attachment |
| created | DateTimeField | Creation date |

---

## Technologies

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- Tailwind CSS
- JavaScript

### Database

- PostgreSQL

### Development Tools

- Docker
- Docker Compose
- Git

---

## Installation

### Clone the repository
git clone https://github.com/nadiabgh/academic_note_organizer.git
cd notes### Install dependencies
pip install -r requirements.txt### Apply migrations
python manage.py migrate### Run the development server
python manage.py runserverOpen your browser:
http://127.0.0.1:8000/---

## Running with Docker

Build the project
docker compose up --buildRun the project
docker compose upStop the containers
docker compose down---

## Running Tests
python manage.py testor
docker compose exec web python manage.py test---


## Project Structure

The project is organized as a Django-based web application following the Model-View-Template (MVT) architecture. The structure separates configuration, application logic, database models, templates, and static resources to maintain a clean and scalable codebase.

The main project directory contains the core Django configuration files:

- settings.py: Defines project configuration, installed applications, database settings, static files configuration, and other Django settings.
- urls.py: Handles the main URL routing and connects different application paths.
- asgi.py and wsgi.py: Provide server configuration for deploying the Django application.

The application contains the main backend components:

- models.py: Defines the database models and relationships between users, courses, and notes.
- views.py: Contains the business logic and handles requests, responses, and data processing.
- urls.py: Defines application-specific URL routes.
- forms.py: Handles user input, validation, and form processing.
- admin.py: Registers models and configures the Django administration interface.
- apps.py: Contains application configuration.

The templates directory contains all HTML files responsible for rendering the user interface. It follows Django's template inheritance system and includes:

- base.html: The main layout template shared across the application, containing common structure, styling references, and reusable components
- registration/: Contains authentication-related templates such as login and signup pages
- courses/: Contains templates for course management, including displaying courses, viewing course details, creating, editing, and deleting courses.
- notes/: Contains templates for note management, including creating, editing, viewing, and deleting notes

The static directory contains frontend resources used by the application:

- CSS files: Define the application's appearance and layout.
- JavaScript files: Handle interactive features and client-side behavior.
- Images and other assets: Store visual resources used throughout the interface.

The media directory stores uploaded files and user-generated content.

Additional project files include:

- manage.py: Django's command-line utility used for running the development server, creating migrations, and managing project operations
- requirements.txt: Contains the project's Python dependencies
- README.md: Provides documentation and information about the project

This organization follows Django's recommended structure by separating backend functionality, database management, user interface templates, and static resources into dedicated sections

---

## Author

Nadia Bagheripour

Computer Science Student  
University of Guilan

---

## License

This project was developed for educational purposes.
