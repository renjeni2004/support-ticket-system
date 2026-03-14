# Support Desk System

A support ticket management system built with Django, MySQL, and Bootstrap 5.
Features Claude AI integration for automatic ticket classification.

## Tech Stack
- Backend: Python, Django, Django REST Framework
- Database: MySQL
- Frontend: HTML, CSS, Bootstrap 5, JavaScript
- AI: Claude LLM (ticket classification)

## Setup Instructions
1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Configure `.env` with your DB credentials and API keys
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`
