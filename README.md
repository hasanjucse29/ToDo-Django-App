

# Django Todo Application

A simple Todo application built with Django. This application allows users to create, edit, and delete tasks. The tasks can be marked as completed or not completed. The project demonstrates the fundamental features of a CRUD (Create, Read, Update, Delete) application.

## Features

- **Create** new tasks.
- **Edit** existing tasks.
- **Delete** tasks without confirmation redirection.
- **View** a list of tasks, showing their completion status.

## Technologies Used

- **Django**  (Backend Framework)
- **HTML/CSS** (Frontend)
- **SQLite** (Default Django Database)

## Prerequisites

Before you begin, make sure you have Python installed. You can check by running:

```bash
python --version
```

You will also need to install Django. You can do this via pip:

```bash
pip install django
```

## Installation and Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

2. **Create a virtual environment:**

```bash
python -m venv myenv
```

3. **Activate the virtual environment:**

   - **Windows:**
   ```bash
   myenv\Scripts\activate
   ```

   - **MacOS/Linux:**
   ```bash
   source myenv/bin/activate
   ```

4. **Install project dependencies:**

```bash
pip install -r requirements.txt
```

5. **Run database migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser (for admin access):**

```bash
python manage.py createsuperuser
```

7. **Run the development server:**

```bash
python manage.py runserver
```

8. **Access the application:**

   - Open your browser and go to `http://127.0.0.1:8000`
   - For admin access, go to `http://127.0.0.1:8000/admin/`

## Project Structure

```
todo_project/
│
├── todo_project/            # Project Configuration Files
│   ├── settings.py          # Django project settings
│   ├── urls.py              # Main URL configuration
│
├── todo/                    # Todo application
│   ├── migrations/          # Database migrations
│   ├── templates/todo/      # HTML templates
│   ├── models.py            # TodoItem model
│   ├── views.py             # Views for handling requests
│   ├── forms.py             # Forms for creating and editing tasks
│   ├── urls.py              # URL configuration for the todo app
│
├── manage.py                # Django project management script
├── README.md                # Project documentation
├── requirements.txt         # List of dependencies
```

## Usage

Once the application is running, you can:

- **Create new tasks:** Click on the "Create New Task" button.
- **Edit tasks:** Click the "Edit" link next to each task to modify its title or completion status.
- **Delete tasks:** Click the "Delete" link to remove tasks without redirection to a confirmation page.

## Styling

Basic styling has been applied using in-line CSS to enhance the UI. Feel free to add more styles or use frameworks like Bootstrap or Tailwind for an improved design.
