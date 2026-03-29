import os

def create_flask_project(name):
    os.makedirs(name, exist_ok=True)

    # folders
    os.makedirs(f"{name}/templates", exist_ok=True)
    os.makedirs(f"{name}/static", exist_ok=True)

    # app.py
    with open(f"{name}/app.py", "w") as f:
        f.write("""from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
""")

    # requirements.txt
    with open(f"{name}/requirements.txt", "w") as f:
        f.write("flask\n")

    print(f"🚀 Flask project '{name}' created!")