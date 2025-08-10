#!/usr/bin/env python3
"""
PaceLock - Entry point script
Runs the main application from the project root.
"""

import sys
import os

# Add src directory to Python path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from api.main import main

if __name__ == "__main__":
    main()