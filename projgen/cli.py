import argparse
from .generator import create_flask_project

def main():
    parser = argparse.ArgumentParser(description="Project Generator")
    parser.add_argument("type", help="project type (flask)")
    parser.add_argument("name", help="project name")

    args = parser.parse_args()

    if args.type == "flask":
        create_flask_project(args.name)
    else:
        print("❌ Unknown project type")