#!/usr/bin/env python
"""
Test runner script for Venus Attendance System
This script helps run tests in the virtual environment.
"""

import os
import subprocess
import sys

def run_tests():
    """Run the test suite"""
    print("Running tests for Venus Attendance System...")
    print("=" * 40)
    
    if os.name == 'nt':  # Windows
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:  # Unix/Linux/Mac
        python_path = os.path.join('venv', 'bin', 'python')
    
    # Check if virtual environment exists
    if not os.path.exists(python_path):
        print("Virtual environment not found. Please run setup.py first.")
        sys.exit(1)
    
    # Run tests
    result = subprocess.run([python_path, 'manage.py', 'test'])
    
    if result.returncode == 0:
        print("\nAll tests passed successfully! ✅")
    else:
        print("\nSome tests failed. ❌")
        sys.exit(result.returncode)

if __name__ == "__main__":
    run_tests()