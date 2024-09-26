# Python Internship Project - Dynamic Web Application
Welcome to the Python Internship Project! This project showcases a dynamic web application built using Django, Python, HTML, CSS, JavaScript, and TailwindCSS. It demonstrates the core functionalities required in the assignment, including web server setup, dynamic content handling, form processing, and data persistence.


## Project Overview
This project was developed as part of a Python internship assignment. It involves creating a basic web page, integrating dynamic content, handling user forms, and persisting form data into a database using Django.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Features](#features) 
3. [Installation Instructions](#Installation-Instructions)
4. [Usage](#usage)


## Technologies Used

- **Python:** Backend programming language.
- **Django:** Web framework for developing the web application, handling routing, form submissions, and rendering templates.
- **HTML/CSS:** For structuring and styling the web pages.
- **JavaScript:** For client-side interactions like live updates of time .
- **TailwindCSS:** Utility-first CSS framework for enhanced styling and responsive design.
- **SQLite:** Default database used for data persistence in Django.


## Features
### **Exercise 1: Basic Web Page**

 A simple HTML/CSS web page was created featuring:
- A header with a title and navigation menu.
- A main content section with some placeholder text.
- A footer containing contact information.

### **Exercise 2: Creating a Python Web Server**

 A Python web server was developed using Django. The server was configured to:
- Serve the HTML/CSS page created in Exercise 1.
- Handle GET requests and return the HTML page with correct routing

### **Exercise 3: Adding Dynamic Content**

 Dynamic content was added to the web page, including:
- A Python function that generates dynamic content such as the current date/time and random quotes.
- This dynamic data is rendered on the webpage using Django templates.

### **Exercise 4 and 5 : Form Handling and Data Persistence**

A form was integrated into the web page to collect user data, and the form submissions are stored in a database for retrieval later.

**Form Handling:**

 - The form collects details such as the user's name and email.
 - A Python route processes the form using POST requests and validates the submitted data.
 - After submission, the user is redirected to a page displaying the submitted information.
  
**Data Persistence:**

 - The form data is stored in a database (SQLite) using Django's ORM (Object-Relational Mapping).
 - A separate route allows retrieval of the stored data, which is displayed on a new page, ensuring data is persistent between sessions.


## Installation Instructions
Follow the steps below to set up and run this Django project locally:

### Prerequisites
- Python 3.12
- Django
- SQLite (default database for Django)

### Setup
 
#### 1. Clone the Repository

```bash
git clone https://github.com/MadhurGupta0/Assignment

cd Assignment

```
#### 2. Create a Virtual Environment
```bash

python -m venv venv
source venv/bin/activate 
```
#### 3. Install Dependencies

```bash
pip install -r Requirements.txt
```
#### 4. Run Migrations and Create a Superuser

```bash

python manage.py makemigrations
python manage.py migrate 
```
#### 5. Run the Django development server:

```bash

python manage.py runserver 
```

#### 6. Access the web application by navigating to http://127.0.0.1:8000/ in your browser.


## Usage
- **Home Page:** The home page contains a basic layout with a header, content section, and footer.
- **Dynamic Content:** The home page displays dynamic content such as the current date and time.
- **Form Submission & Data Persistence:**
  - The form collects user information, including the name and email address.
  - Submitted data is saved to the SQLite database.
  - A separate page allows you to view previously submitted data, demonstrating data persistence.

 
