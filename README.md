# To-Do Web App (Flask)

A simple To-Do web application built using Flask.  
Users can add, update, delete, and mark tasks as completed.

This project was created for learning Flask, templates, and basic database operations.

---

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as completed
- Data stored using SQLAlchemy

---

## Tech Used

- Python
- Flask
- HTML
- CSS / SCSS
- SQLAlchemy

---

## Project Structure

```

To-Do-Web-app/
├── app.py
├── requirements.txt
├── instance/
│   └── database.db
├── static/
│   ├── css/
│   │   └── style.css
│   └── scss/
│       └── style.scss
├── templates/
│   ├── base.html
│   ├── index.html
│   └── edit.html
└── README.md

````

---

## How to Run

1. Clone the repository
```bash
git clone https://github.com/Md-Afzaal/To-Do.git
cd To-Do
````

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
python app.py
```

4. Open browser and visit

```
http://127.0.0.1:5000/
```

---

## SCSS Compilation

SCSS must be compiled before styles work.

```bash
sass static/scss/style.scss static/css/style.css
```

For auto compile:

```bash
sass --watch static/scss:static/css
```

---

## Author

Mohd Afzaal

