# food.com
This is a food web application with comprehensive login functionality and testing.

## Features
- Clean, responsive login interface
- Secure user authentication
- Session management
- Form validation
- Error handling with user feedback
- Comprehensive test suite

## Login Button Testing

The login button has been thoroughly tested with a comprehensive test suite including:

### Automated Tests (17 test cases)
- **Functionality Tests**: Login page loading, button existence, valid/invalid login attempts
- **Security Tests**: SQL injection prevention, XSS protection
- **UI/UX Tests**: CSS styling, hover effects, accessibility features
- **Form Validation**: Empty fields, partial credentials, case sensitivity

### Test Accounts
For testing purposes, use these pre-configured accounts:
- Username: `admin`, Password: `password123`
- Username: `user`, Password: `userpass`
- Username: `test`, Password: `testpass`

## Running the Application

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser to: `http://127.0.0.1:5000`

## Running Tests

### Automated Testing
Run the complete test suite:
```bash
python -m pytest test_login_button.py -v
```

Or use the test runner script:
```bash
./run_login_tests.sh
```

### Manual Testing
1. Start the application with `python app.py`
2. Navigate to the login page
3. Test valid credentials (see test accounts above)
4. Test invalid credentials to verify error handling
5. Test the logout functionality

## Login Button Features Tested

✅ **Core Functionality**
- Login form submission
- Credential validation
- Session management
- Redirect behavior

✅ **Security**
- Input sanitization
- Protection against injection attacks
- Secure session handling

✅ **User Experience**
- Clear error messages
- Visual feedback
- Responsive design
- Accessibility features

✅ **Form Validation**
- Required field validation
- Empty input handling
- Case-sensitive authentication
