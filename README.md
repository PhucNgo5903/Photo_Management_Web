## PhotoShare
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Demo](#demo)

## Introduction
Photo Management Web is a web-based application that allows users to upload, store, and manage their personal photos. This application provides a secure and user-friendly interface for handling image files, offering an easy way to organize and access your photo collection online.

## Features
- **User Authentication:** Secure user registration and login system.
- **Photo Upload:** Users can upload their personal photos.
- **Photo Management:** Users can view, delete, and organize their uploaded photos.
- **Responsive Design:** Fully responsive design that works on all devices.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Django, Python
- **Database:** SQLite (default)
- **Other Tools:** Django Crispy Forms, Pillow

## Installation
Follow these steps to get a local copy of the project up and running:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/PhucNgo5903/Photo_Management_Web.git
    cd Photo_Management_Web
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
    ```bash
    pip install django
    pip install django-crispy-forms
    pip install crispy-bootstrap4
    pip install Pillow
    pip install django-storages
    ```

4. **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
Once the server is running, open your web browser and navigate to `http://127.0.0.1:8000/`. Log in with your credentials to start uploading and managing your photos.

## Testing
To run the tests, use the following command:
```bash
python manage.py test
