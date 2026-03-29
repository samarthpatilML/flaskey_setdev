# Flaskey SetDev 🚀

A simple CLI tool to quickly generate Python project templates (like Flask apps) in seconds.

---

## 📦 Installation

Install the package using pip:

```bash
pip install flaskey-setdev
```

---

## ⚡ Usage

Create a new project using:

```bash
create-project flask myapp
```

This will generate a folder like:

```
myapp/
├── app.py
├── requirements.txt
├── templates/
├── static/
```

---

## 🧰 Available Commands

### 🔹 Create Flask Project

```bash
create-project flask <project_name>
```

Example:

```bash
create-project flask mywebsite
```

---

## 📁 Generated Files

* `app.py` → Basic Flask application
* `requirements.txt` → Required dependencies
* `templates/` → HTML templates folder
* `static/` → CSS/JS files folder

---

## 💡 Requirements

* Python 3.7 or higher
* pip installed

---

## 🛠️ Troubleshooting

### Command not found?

If you see:

```
'create-project' is not recognized
```

👉 Add this folder to your PATH:

```
C:\Users\<YourUsername>\AppData\Roaming\Python\PythonXX\Scripts
```

Then restart your terminal.

---

## 👨‍💻 Author

Samarth Patil

---

## ⭐ Future Features

* FastAPI project generator
* Django starter template
* Virtual environment auto setup
* Git initialization

---

## ❤️ Support

If you like this project, consider giving it a ⭐ on GitHub!
