#!/bin/bash

# PaceLock Setup Script
# Creates virtual environment and installs dependencies

set -e

echo "🚀 Setting up PaceLock development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
echo "📋 Installing Python dependencies..."
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To activate the virtual environment in your shell:"
echo "  source venv/bin/activate"
echo ""
echo "To run the application:"
echo "  npm run dev"