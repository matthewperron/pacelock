#!/bin/bash

# PaceLock Development Script
# Activates virtual environment and runs the application

if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run 'npm run setup' first."
    exit 1
fi

echo "🏃 Running PaceLock..."
source venv/bin/activate
python main.py