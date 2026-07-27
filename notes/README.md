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

## Entity Relationship
User
 │
 └──── Course
          │
          └──── Note (A user can create multiple courses, and each course can contain multiple notes)

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
Notanizer/
│
├── Notanizer/
│   ├── migrations/
│   │   └── Database migration files
│   │
│   ├── static/
│   │   └── CSS, JavaScript, images, fonts, and other static assets
│   │
│   ├── templates/
│   │   ├── courses/
│   │   │   └── Course-related templates
│   │   ├── notes/
│   │   │   └── Note-related templates
│   │   ├── registration/
│   │   │   └── Login and sign-up templates
│   │   └── search/
│   │       └── Search results template
│   │
│   ├── models.py
│   │   └── Defines the User, Course, and Note models
│   │
│   ├── views.py
│   │   └── Handles application logic and HTTP requests
│   │
│   ├── forms.py
│   │   └── Defines Django forms for authentication, courses, and notes
│   │
│   ├── urls.py
│   │   └── URL routing for the application
│   │
│   ├── tests.py
│   │   └── Unit tests for models and views
│   │
│   ├── admin.py
│   │   └── Registers models for the Django admin panel
│   │
│   └── ...
│
├── media/
│   └── Stores uploaded images and files
│
├── Dockerfile
│   └── Docker image configuration
│
├── docker-compose.yml
│   └── Defines the Docker services(web and PostgreSQL)
│
├── requirements.txt
│   └── Python project dependencies
│
├── manage.py
│   └── Django command-line utility
│
└── README.md
    └── Project documentation
---

## Author

Nadia Bagheripour

Computer Science Student  
University of Guilan

---

## License

This project was developed for educational purposes.