#!/usr/bin/env python
"""
Root-level Django management script.
Allows running `python manage.py <command>` directly from the project root.
"""
import os
import sys
from pathlib import Path

# Add Code/mysite to sys.path so mysite and polls are importable
BASE_DIR = Path(__file__).resolve().parent
DJANGO_DIR = BASE_DIR / "Code" / "mysite"

if str(DJANGO_DIR) not in sys.path:
    sys.path.insert(0, str(DJANGO_DIR))

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
