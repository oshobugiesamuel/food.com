#!/bin/bash

# Test Runner for Login Button Functionality
# This script runs all tests for the login button

echo "========================================="
echo "Food.com Login Button Test Suite"
echo "========================================="

echo ""
echo "1. Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "2. Running automated tests..."
python -m pytest test_login_button.py -v

echo ""
echo "3. Test Summary:"
echo "   - Total tests: 17"
echo "   - Testing login button functionality"
echo "   - Testing form validation"
echo "   - Testing security features"
echo "   - Testing UI/UX elements"

echo ""
echo "4. Manual Testing Instructions:"
echo "   To manually test the login button:"
echo "   a) Run: python app.py"
echo "   b) Open browser to: http://127.0.0.1:5000"
echo "   c) Test valid login with:"
echo "      - Username: admin, Password: password123"
echo "      - Username: user, Password: userpass"
echo "      - Username: test, Password: testpass"
echo "   d) Test invalid login with wrong credentials"
echo "   e) Verify error messages and redirects work properly"

echo ""
echo "========================================="
echo "Login Button Testing Complete!"
echo "========================================="