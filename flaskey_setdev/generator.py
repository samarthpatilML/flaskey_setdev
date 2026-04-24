import os
import subprocess
import sys
import platform

def create_flask_project(name):
    os.makedirs(name, exist_ok=True)

    templates_path = os.path.join(name, "templates")
    static_path = os.path.join(name, "static")
    os.makedirs(templates_path, exist_ok=True)
    os.makedirs(static_path, exist_ok=True)

    # app.py
    with open(os.path.join(name, "app.py"), "w", encoding="utf-8") as f:
        f.write("""from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
""")

    # requirements.txt
    with open(os.path.join(name, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write("flask\n")

    # index.html
    with open(os.path.join(templates_path, "index.html"), "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Starter</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
<nav class="navbar navbar-dark bg-dark">
  <div class="container">
    <span class="navbar-brand mb-0 h1">Flaskey</span>
  </div>
</nav>
<div class="container d-flex align-items-center justify-content-center" style="height: 90vh;">
  <div class="text-center">
    <h1 class="display-4 fw-bold">Build Something Amazing</h1>
    <p class="lead text-muted">Your Flask app is ready with modern UI.</p>
    <div class="mt-4">
      <a href="#" class="btn btn-primary btn-lg me-2">Get Started</a>
      <a href="#" class="btn btn-outline-secondary btn-lg">Docs</a>
    </div>
  </div>
</div>
</body>
</html>
""")

    # style.css
    with open(os.path.join(static_path, "style.css"), "w", encoding="utf-8") as f:
        f.write("""body {
    background: linear-gradient(to right, #f8f9fa, #e9ecef);
}
""")

    # .gitignore  ← NEW
    with open(os.path.join(name, ".gitignore"), "w", encoding="utf-8") as f:
        f.write("venv/\n__pycache__/\n*.pyc\n.env\n")

    # Cross-platform venv setup  ← FIXED
    print("🔧 Creating virtual environment...")
    venv_path = os.path.join(name, "venv")
    subprocess.check_call([sys.executable, "-m", "venv", venv_path])

    is_windows = platform.system() == "Windows"
    pip_path = os.path.join(
        venv_path,
        "Scripts" if is_windows else "bin",
        "pip"
    )

    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([
            pip_path, "install", "-r",
            os.path.join(name, "requirements.txt")
        ])
    except subprocess.CalledProcessError as e:
        print(f"❌ Dependency install failed: {e}")
        sys.exit(1)

    print(f"✅ Flask project '{name}' is READY!")
    print(f"\n👉 To run your app:")
    print(f"   cd {name}")
    if is_windows:
        print(f"   venv\\Scripts\\activate")
    else:
        print(f"   source venv/bin/activate")
    print(f"   python app.py")