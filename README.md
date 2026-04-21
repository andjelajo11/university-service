# 📚 Student & Professor Management Console App

## 🧾 Overview

This is a Python console-based application for managing students and professors.
It allows users to register, log in, and access role-specific functionalities depending on whether they are a **student** or a **professor**.

The system uses simple file-based storage:

* **CSV** for professors
* **JSON** for students

---

## ⚙️ Features

### 🔐 Authentication

* User registration (Student / Professor)
* Login system with role-based access
* Session tracking via a global logged-in user

### 👨‍🏫 Professor

* Register with:

  * Username (3 digits)
  * Password
  * Name & surname
  * Email
  * Consultation term
* Data stored in `data/profesori.csv`
* Access to professor-specific menu (`menu_prof`)

### 🎓 Student

* Register with:

  * Index number (must be unique)
  * Password
  * Name & surname
  * Email
* Data stored in `data/studenti.json`
* Each student has an `ocene` (grades) list
* Access to student-specific menu (`menu_stud`)

---

## 🗂️ Project Structure

```
project/
│
├── main.py
├── dodatno.py
├── profesorMeni.py
├── studentMeni.py
│
└── data/
    ├── profesori.csv
    └── studenti.json
```

---

## ▶️ How to Run

1. Make sure you have Python 3 installed
2. Run the main file:

```bash
python main.py
```

---

## 🧭 Application Flow

### Main Menu

```
A: Registration
B: Login
Q: Exit
```

### Registration

* Choose:

  * `P` → Professor
  * `S` → Student

### Login

* Professors log in using:

  * Username (`sifra`)
  * Password

* Students log in using:

  * Index number
  * Password

After successful login, users are redirected to their respective menus.

---

## 💾 Data Storage

### Professors (`CSV`)

Stored as rows:

```
username, password, firstname, surname, email, consultation_term
```

### Students (`JSON`)

Stored as objects:

```json
{
  "indeks": 123,
  "lozinka": "password",
  "ime": "Name",
  "prezime": "Surname",
  "email": "email@example.com",
  "ocene": []
}
```

---

## 📌 Dependencies

Standard Python libraries only:

* `os`
* `json`
* `csv`
* `sys`

---

## 🚧 Future Improvements

* Add password hashing for security
* Improve input validation
* Add persistent session handling

---

## 👩‍💻 Author

Developed as a console-based academic management system project.


