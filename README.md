# Workshop Management System

## Overview
The **Workshop Management System** is a web-based application designed to streamline the process of organizing and managing workshops. This system allows users to create, update, view, and delete workshops efficiently. It also provides a REST API for external integrations using Django REST Framework (DRF).

## Features
- **Workshop CRUD Operations**: Create, read, update, and delete workshops.
- **User-friendly Interface**: Interactive web pages using Django templates.
- **REST API Support**: Exposes API endpoints for seamless integration with other systems.
- **MySQL Database**: Stores workshop details securely.
- **Admin Panel**: Manage workshops via Django’s built-in admin interface.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (Django templates)
- **Database**: MySQL
- **Version Control**: Git & GitHub
- **Development Tools**: Python, Virtual Environment, MySQL Workbench

## Installation and Setup

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- MySQL Server
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/username/workshop-management-system.git
cd workshop-management-system
```

### Step 2: Set Up a Virtual Environment
#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Database
1. Create a MySQL database:
```sql
CREATE DATABASE workshop_db;
```
2. Update `settings.py` with your database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'workshop_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Step 5: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/` | Retrieve all workshops |
| GET | `/api/<id>/` | Retrieve a specific workshop |
| POST | `/api/` | Create a new workshop |
| PUT | `/api/<id>/` | Update a workshop |
| DELETE | `/api/<id>/` | Delete a workshop |

## Deployment
For production deployment:
- Use a WSGI server like Gunicorn
- Configure `DEBUG = False` in `settings.py`
- Set up `ALLOWED_HOSTS`

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Author
[P.R.P. Dhananjaya Bandara](https://github.com/username)

## Contributions
Contributions are welcome! Feel free to submit a pull request or report issues.

