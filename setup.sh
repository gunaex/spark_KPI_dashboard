#!/bin/bash

# Setup script for KPI Dashboard

echo "======================================"
echo "KPI Dashboard Setup"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Check Java installation
echo ""
echo "Checking Java installation..."
if command -v java &> /dev/null; then
    java_version=$(java -version 2>&1 | head -n 1)
    echo "Java found: $java_version"
else
    echo "WARNING: Java not found. Apache Spark requires Java 8 or higher."
    echo "Please install Java before continuing."
    exit 1
fi

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "✗ Failed to install dependencies"
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file..."
    cp config/.env.example .env
    echo "✓ .env file created"
fi

# Run tests
echo ""
echo "Running tests..."
python -m unittest discover src/tests/ -v

if [ $? -eq 0 ]; then
    echo ""
    echo "======================================"
    echo "✓ Setup completed successfully!"
    echo "======================================"
    echo ""
    echo "To start the dashboard, run:"
    echo "  python app.py"
    echo ""
    echo "Then open your browser to: http://localhost:5000"
else
    echo ""
    echo "✗ Tests failed. Please check the errors above."
    exit 1
fi
