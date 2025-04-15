# Student Portal API

A Django REST Framework-based API for managing student information in a student portal.

## Features

- Manage student profiles
- Course enrollment and management
- Grade tracking
- Authentication and authorization

## Requirements

- Python 3.10+
- Django 5.0
- Django REST Framework

## Reference(s)

> 1. [Django REST Framework](https://www.django-rest-framework.org/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Swamy-s-Tech-Skills-Academy/student-portal-api.git
   cd student-portal-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   pip freeze  # Should show no packages installed
   ```

3. Install dependencies:

   ```bash
   pip install django
   pip install --upgrade pip
   pip install djangorestframework
   pip freeze # It should show the installed packages
   pip freeze > requirements.txt
   ```

4. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. Create the Django project:

> 1. (.venv) PS D:\STSA\student-portal-api\src>
> 2. Create a new Django project

```bash
    django-admin startproject student_portal_main .
    cd src
```

6. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Access the API at `http://127.0.0.1:8000/`.
- Use tools like Postman to test the endpoints.

## Folder Structure

```text
student-portal-api/
├── LICENSE
├── README.md
├── docs/
│   └── images/
├── src/
│   ├── manage.py
│   ├── student_portal/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── students/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── static/
│   └── templates/
├── requirements.txt
```

- **LICENSE**: Contains the license information for the project.
- **README.md**: Project documentation and setup instructions.
- **docs/**: Documentation-related files.
  - **images/**: Images used in the documentation.
- **src/**: Source code for the Django project.
  - **manage.py**: Django's command-line utility for administrative tasks.
  - **student_portal/**: Main project folder containing settings and configurations.
    - **settings.py**: Configuration for the project.
    - **urls.py**: URL routing for the project.
    - **wsgi.py**: Entry point for WSGI-compatible web servers.
    - **asgi.py**: Entry point for ASGI-compatible web servers.
  - **students/**: App for managing student-related features.
    - **models.py**: Database models for the app.
    - **serializers.py**: Serializers for converting data to/from JSON.
    - **views.py**: Views for handling API requests.
    - **tests.py**: Test cases for the app.
    - **admin.py**: Admin interface configurations.
    - **apps.py**: App configuration.
    - **migrations/**: Database migration files.
  - **static/**: Static files (CSS, JavaScript, images).
  - **templates/**: HTML templates for the project.
- **requirements.txt**: List of dependencies for the project.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
