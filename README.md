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

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Swamy-s-Tech-Skills-Academy/student-portal-api.git
   cd student-portal-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   source env/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the API at `http://127.0.0.1:8000/`.
- Use tools like Postman to test the endpoints.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
