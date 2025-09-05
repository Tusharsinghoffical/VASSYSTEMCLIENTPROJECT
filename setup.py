#!/usr/bin/env python
"""
Setup script for Venus Attendance System
This script helps automate the setup process for new developers.
"""

import os
import sys
import subprocess
import venv

def create_virtual_environment():
    """Create a virtual environment"""
    print("Creating virtual environment...")
    venv.create('venv', with_pip=True)
    print("Virtual environment created successfully!")

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    if os.name == 'nt':  # Windows
        pip_path = os.path.join('venv', 'Scripts', 'pip')
    else:  # Unix/Linux/Mac
        pip_path = os.path.join('venv', 'bin', 'pip')
    
    subprocess.run([pip_path, 'install', '-r', 'requirements.txt'])
    print("Dependencies installed successfully!")

def run_migrations():
    """Run database migrations"""
    print("Running database migrations...")
    if os.name == 'nt':  # Windows
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:  # Unix/Linux/Mac
        python_path = os.path.join('venv', 'bin', 'python')
    
    subprocess.run([python_path, 'manage.py', 'migrate'])
    print("Database migrations completed!")

def create_superuser():
    """Create a superuser account"""
    print("Creating superuser account...")
    if os.name == 'nt':  # Windows
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:  # Unix/Linux/Mac
        python_path = os.path.join('venv', 'bin', 'python')
    
    subprocess.run([python_path, 'manage.py', 'createsuperuser'])
    print("Superuser account created!")

def main():
    """Main setup function"""
    print("Welcome to the Venus Attendance System Setup!")
    print("=" * 50)
    
    try:
        create_virtual_environment()
        install_dependencies()
        run_migrations()
        
        create_superuser_choice = input("\nWould you like to create a superuser account? (y/n): ")
        if create_superuser_choice.lower() == 'y':
            create_superuser()
        
        print("\nSetup completed successfully!")
        print("\nTo start the development server, run:")
        if os.name == 'nt':  # Windows
            print("  venv\\Scripts\\python manage.py runserver")
        else:  # Unix/Linux/Mac
            print("  venv/bin/python manage.py runserver")
        
        print("\nThen open your browser to http://127.0.0.1:8000/")
        
    except Exception as e:
        print(f"An error occurred during setup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()