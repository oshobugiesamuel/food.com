import pytest
from app import app, USERS


@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    with app.test_client() as client:
        yield client


@pytest.fixture
def session_client():
    """Create a client with session support for testing."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess['_csrf_token'] = 'test-token'
        yield client


class TestLoginButton:
    """Test suite for login button functionality."""

    def test_login_page_loads(self, client):
        """Test that the login page loads successfully."""
        response = client.get('/login')
        assert response.status_code == 200
        assert b'Food.com Login' in response.data
        assert b'login-button' in response.data

    def test_login_button_exists(self, client):
        """Test that the login button is present on the login page."""
        response = client.get('/login')
        assert b'id="login-button"' in response.data
        assert b'type="submit"' in response.data
        assert b'Login' in response.data

    def test_login_button_css_class(self, client):
        """Test that the login button has the correct CSS class."""
        response = client.get('/login')
        assert b'class="login-button"' in response.data

    def test_valid_login_via_button(self, client):
        """Test successful login using the login button."""
        login_data = {
            'username': 'admin',
            'password': 'password123'
        }
        response = client.post('/login', data=login_data, follow_redirects=True)
        assert response.status_code == 200
        assert b'Welcome admin!' in response.data
        assert b'Logout' in response.data

    def test_invalid_login_via_button(self, client):
        """Test unsuccessful login with wrong credentials."""
        login_data = {
            'username': 'invalid_user',
            'password': 'wrong_password'
        }
        response = client.post('/login', data=login_data)
        assert response.status_code == 200
        assert b'Invalid username or password!' in response.data
        assert b'login-button' in response.data  # Still on login page

    def test_empty_credentials_login_button(self, client):
        """Test login button behavior with empty credentials."""
        login_data = {
            'username': '',
            'password': ''
        }
        response = client.post('/login', data=login_data)
        assert response.status_code == 200
        # Should stay on login page due to validation errors
        assert b'login-button' in response.data

    def test_login_button_with_partial_credentials(self, client):
        """Test login button with only username or only password."""
        # Only username
        response = client.post('/login', data={'username': 'admin', 'password': ''})
        assert response.status_code == 200
        assert b'login-button' in response.data
        
        # Only password
        response = client.post('/login', data={'username': '', 'password': 'password123'})
        assert response.status_code == 200
        assert b'login-button' in response.data

    def test_multiple_user_logins_via_button(self, client):
        """Test login button works for different valid users."""
        for username, password in USERS.items():
            login_data = {
                'username': username,
                'password': password
            }
            response = client.post('/login', data=login_data, follow_redirects=True)
            assert response.status_code == 200
            assert f'Welcome {username}!'.encode() in response.data
            
            # Logout for next test
            client.get('/logout')

    def test_login_button_redirect_behavior(self, client):
        """Test that successful login redirects properly."""
        login_data = {
            'username': 'test',
            'password': 'testpass'
        }
        response = client.post('/login', data=login_data, follow_redirects=False)
        assert response.status_code == 302  # Redirect
        assert response.location.endswith('/')

    def test_login_button_case_sensitivity(self, client):
        """Test that login is case-sensitive."""
        login_data = {
            'username': 'ADMIN',  # Wrong case
            'password': 'password123'
        }
        response = client.post('/login', data=login_data)
        assert response.status_code == 200
        assert b'Invalid username or password!' in response.data

    def test_login_button_form_method(self, client):
        """Test that the login form uses POST method."""
        response = client.get('/login')
        assert b'method="POST"' in response.data

    def test_login_button_accessibility(self, client):
        """Test login button accessibility features."""
        response = client.get('/login')
        # Check for proper form labels and structure
        assert b'Username' in response.data
        assert b'Password' in response.data
        assert b'id="username"' in response.data
        assert b'id="password"' in response.data
        assert b'id="login-button"' in response.data


class TestLoginButtonSecurity:
    """Security-focused tests for the login button."""

    def test_login_button_prevents_sql_injection_attempt(self, client):
        """Test that login button doesn't process SQL injection attempts."""
        malicious_data = {
            'username': "admin'; DROP TABLE users; --",
            'password': 'password123'
        }
        response = client.post('/login', data=malicious_data)
        assert response.status_code == 200
        assert b'Invalid username or password!' in response.data

    def test_login_button_prevents_script_injection(self, client):
        """Test that login button doesn't execute script injections."""
        malicious_data = {
            'username': '<script>alert("xss")</script>',
            'password': 'password123'
        }
        response = client.post('/login', data=malicious_data)
        assert response.status_code == 200
        assert b'Invalid username or password!' in response.data


class TestLoginButtonUI:
    """UI and user experience tests for the login button."""

    def test_login_button_styling_classes(self, client):
        """Test that login button has proper CSS styling."""
        response = client.get('/login')
        assert b'login-button' in response.data
        # Check for CSS styles in the response
        assert b'background-color: #007bff' in response.data
        assert b'cursor: pointer' in response.data

    def test_login_button_hover_effects(self, client):
        """Test that login button has hover effects defined."""
        response = client.get('/login')
        assert b'.login-button:hover' in response.data
        assert b'background-color: #0056b3' in response.data

    def test_login_button_focus_effects(self, client):
        """Test that login button has focus effects for accessibility."""
        response = client.get('/login')
        assert b'.login-button:focus' in response.data
        assert b'box-shadow' in response.data