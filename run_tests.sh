#!/bin/bash

# Activate the virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate  # macOS/Linux
elif [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate  # Windows
else
    echo "Virtual environment not found!"
    exit 1
fi

# Run tests
pytest tests/test_app.py --headless
TEST_RESULT=$?

# Deactivate virtual environment
deactivate

# Return exit code based on test results
if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
