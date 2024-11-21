#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def check_dependencies() -> None:
    """Check if all required dependencies are installed."""
    try:
        import django
    except ImportError:
        raise ImportError(
            "Django is not installed. Please install it with: pip install django"
        )

    required_packages = ['rest_framework', 'django_filters']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        raise ImportError(
            f"The following required packages are missing: {', '.join(missing_packages)}\n"
            f"Please install them with: pip install {' '.join(missing_packages)}"
        )


def check_python_version() -> None:
    """Check if Python version meets the minimum requirement."""
    min_version = (3, 8)
    current_version = sys.version_info[:2]

    if current_version < min_version:
        raise RuntimeError(
            f"Python {min_version[0]}.{min_version[1]} or higher is required. "
            f"Current version is {current_version[0]}.{current_version[1]}"
        )


def main() -> None:
    """Run administrative tasks."""
    try:
        # Perform checks
        check_python_version()
        check_dependencies()
        
        # Set the default settings module
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        
        execute_from_command_line(sys.argv)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
