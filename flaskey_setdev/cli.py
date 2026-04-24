import argparse
import sys
from .generator import create_flask_project

SUPPORTED_TYPES = ["flask"]

def main():
    parser = argparse.ArgumentParser(
        prog="flaskey",
        description="⚡ Flaskey — Flask project generator",
        epilog="Example: flaskey flask my_app"
    )

    parser.add_argument(
        "type",
        choices=SUPPORTED_TYPES,          # ← argparse rejects invalid types automatically
        metavar="type",                    # ← shows 'type' in help instead of '{flask}'
        help=f"project type to generate. Supported: {', '.join(SUPPORTED_TYPES)}"
    )

    parser.add_argument(
        "name",
        help="name of the project folder to create"
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version="%(prog)s 1.0.0"           # ← bump this when you release
    )

    # Print help if called with no arguments
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    handlers = {
        "flask": create_flask_project,     # ← easy to extend with django, fastapi, etc.
    }

    handler = handlers.get(args.type)
    if handler:
        handler(args.name)
    else:
        print(f"❌ Unknown project type: '{args.type}'", file=sys.stderr)
        sys.exit(1)