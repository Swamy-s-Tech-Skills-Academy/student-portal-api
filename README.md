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

## Creating the "students" App

To create the `students` app for managing student-related features, follow these steps:

1. Navigate to the `src` directory:

   ```bash
   cd src
   ```

2. Create the `students` app using Django's `startapp` command:

   ```bash
   python manage.py startapp students
   ```

3. Add the `students` app to the `INSTALLED_APPS` list in `student_portal_main/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...existing apps...
       'students',
   ]
   ```

4. Define models for the `students` app in `students/models.py`.

5. Run migrations to apply any changes:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create views, serializers, and URLs for the `students` app as needed.

> 1. [Students endpoints](http://127.0.0.1:8000/students/) - This URL will be used to access the student portal.

## Creating the "api" App

To create the `api` app for managing API-related logic, follow these steps:

1. Navigate to the `src` directory:

   ```bash
   cd src
   ```

2. Create the `api` app using Django's `startapp` command:

   ```bash
   python manage.py startapp api
   ```

3. Add the `api` app to the `INSTALLED_APPS` list in `student_portal_main/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...existing apps...
       'api',
   ]
   ```

4. Define serializers, views, and URLs for the `api` app as needed.

5. Run migrations to apply any changes (if models are added):

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Organize API versions (if needed) by creating subdirectories within the `api` app, such as `api/v1/` or `api/v2/`.

> 1. [Students endpoints](http://127.0.0.1:8000/api/v1/students/) - This URL will be used to access the API endpoints for the `students` app.

## Folder Structure After Adding the "api" App

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
│   ├── api/
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

- **api/**: App for managing API-related logic.
  - **models.py**: Database models for the app (if needed).
  - **serializers.py**: Serializers for converting data to/from JSON.
  - **views.py**: Views for handling API requests.
  - **tests.py**: Test cases for the app.
  - **admin.py**: Admin interface configurations.
  - **apps.py**: App configuration.
  - **migrations/**: Database migration files.

## API Endpoints

### Students List Endpoint

- **URL**: `/students/`
- **Method**: GET
- **Description**: Retrieves a list of all students.
- **Response**:

  ```json
  [
    { "name": "John Doe", "age": 20 },
    { "name": "Jane Smith", "age": 22 },
    { "name": "Alice Johnson", "age": 19 }
  ]
  ```

- **Example Request**:
  ```bash
  curl -X GET http://127.0.0.1:8000/students/
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
│   ├── api/
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
  - **api/**: App for managing API-related logic.
    - **models.py**: Database models for the app (if needed).
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
