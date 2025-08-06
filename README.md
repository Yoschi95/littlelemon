# Back‑End Developer Capstone – Little Lemon API

**(Coursera | Meta Back‑End Developer Professional Certificate)**

## 📘 Overview

This repository hosts the **Module 4 Capstone project** for the **Meta Back‑End Developer Professional Certificate** on Coursera. In this course you build a **Django REST API** for a fictional restaurant ("Little Lemon") to demonstrate practical backend development skills including:

- Creating a Django server with multiple API endpoints
- Connecting to a MySQL database
- Implementing models, serializers, views, and template-driven HTML pages
- User registration and authentication workflows
- Unit testing and API testing with Insomnia
- Version control using Git and GitHub

## 🧰 Key Features

- **Models & Database**: Django models for menu items, bookings, and user accounts; backed by MySQL
- **REST API**: CRUD endpoints for menus and table bookings using Django REST Framework
- **Security**: User registration, login/logout, authentication-protected endpoints
- **Frontend Templates**: Minimal static HTML views powered by Django templates
- **Testing**: Unit tests for backend logic + Insomnia collections for API testing
- **Deployment-ready**: Config scripts for local and production setups

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd LittleLemon
   ```
2. Install dependencies:
   ```
   pipenv install
   ```
3. Activate the virtual environment:
   ```
   pipenv shell
   ```
4. Prepare database:
   ```
   python manage.py makemigrations
   ```
5. Create database:
   ```
   python manage.py migrate
   ```
6. Run the server:
   ```
   python manage.py runserver
   ```

## Requirements

- Python 3.12
- pipenv

## APIs

```
Create user
http://127.0.0.1:8000/auth/users/

Get token
http://127.0.0.1:8000/auth/token/login/

Menu API
http://127.0.0.1:8000/restaurant/menu/

Booking API
http://127.0.0.1:8000/restaurant/booking/tables/
```

## License

This project is licensed under the MIT License.
