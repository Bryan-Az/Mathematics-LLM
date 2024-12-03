#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install dependencies if needed
pip install -r requirements.txt

# Run tests with coverage
pytest --cov=. --cov-report=term-missing --cov-report=html

# Open coverage report if on a desktop system
if [ -f "htmlcov/index.html" ]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open htmlcov/index.html
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open htmlcov/index.html
    elif [[ "$OSTYPE" == "msys" ]]; then
        start htmlcov/index.html
    fi
fi
