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
```
Thank you for checking out PhotoShare! 

## DEMO:
Home page:
![image](https://github.com/user-attachments/assets/5689ec0d-71a1-4dca-a935-12773d370f8d)

Registration page:
![image](https://github.com/user-attachments/assets/a0919904-32ca-452a-955f-303affa330a3)

Login page:
![image](https://github.com/user-attachments/assets/6640a046-3d4a-4a31-9806-11a8438124dd)

Profile:
![image](https://github.com/user-attachments/assets/76f606e6-916e-4186-8b76-0577bbf5a169)


Gallery:
![image](https://github.com/user-attachments/assets/ed1c31ca-28ac-4dbf-bcd2-0ee8ecb310c5)

![image](https://github.com/user-attachments/assets/895ff5e2-2aa0-4dcc-84a2-e43fad06c199)

View photo:
![image](https://github.com/user-attachments/assets/82f4ce4a-3be8-4d65-8e6d-1a6dbea779df)




















