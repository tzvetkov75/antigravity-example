# Audo added TEXT-123
import sys
import unittest
from unittest.mock import MagicMock, patch

# Mock mysql, flask, and werkzeug BEFORE importing app
mock_mysql = MagicMock()
sys.modules['mysql'] = mock_mysql
sys.modules['mysql.connector'] = mock_mysql

mock_flask = MagicMock()
sys.modules['flask'] = mock_flask

mock_flask_wtf = MagicMock()
sys.modules['flask_wtf'] = mock_flask_wtf
sys.modules['flask_wtf.csrf'] = mock_flask_wtf

mock_werkzeug = MagicMock()
sys.modules['werkzeug'] = mock_werkzeug
sys.modules['werkzeug.security'] = mock_werkzeug

# Setup Flask mock to behave nicely
mock_app_instance = MagicMock()
def route_decorator(*args, **kwargs):
    def wrapper(f):
        return f
    return wrapper

mock_app_instance.route.side_effect = route_decorator
mock_flask.Flask.return_value = mock_app_instance
mock_flask.render_template.return_value = "Rendered Template"

# Mock generate_password_hash to return a predictable value
mock_werkzeug.generate_password_hash.side_effect = lambda p: f"hashed_{p}"

# Now we can import app
try:
    from app import app, index
except ImportError:
    app = None
    index = None

class TestWebApp(unittest.TestCase):
    def setUp(self):
        if app is None:
            self.skipTest("App could not be imported")

    @patch('app.get_db_connection')
    @patch('app.add_user')
    @patch('app.request')
    @patch('app.flash')
    def test_add_user_logic(self, mock_flash, mock_request, mock_add_user, mock_get_conn):
        """Test adding a user logic directly on index function."""
        # Setup mocks
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Configure Request
        mock_request.method = 'POST'
        mock_request.form.get.side_effect = lambda k: {
            'action': 'add',
            'username': 'Web User',
            'email': 'web@test.com',
            'password': 'webpassword'
        }.get(k)
        
        # Call the view function directly
        index()
        
        # Check if add_user was called with HASHED password
        # checking against 'hashed_webpassword' because of our mock side_effect
        mock_add_user.assert_called_with(mock_cursor, 'Web User', 'web@test.com', 'hashed_webpassword')
        mock_flash.assert_called_with('User Web User added successfully!', 'success')

    @patch('app.get_db_connection')
    @patch('app.get_user_by_name')
    @patch('app.request')
    @patch('app.render_template')
    def test_search_user_logic(self, mock_render, mock_request, mock_get_user, mock_get_conn):
        """Test searching for a user logic directly."""
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        # Mock finding a user
        mock_get_user.return_value = ('Found User', 'found@test.com')
        
        mock_request.method = 'POST'
        mock_request.form.get.side_effect = lambda k: {
            'action': 'search',
            'search_username': 'Found User'
        }.get(k)
        
        index()
        
        # Check calls
        mock_get_user.assert_called_with(mock_cursor, 'Found User')
        mock_render.assert_called()
        # Verify search_result was passed to render_template
        call_args = mock_render.call_args
        self.assertEqual(call_args[1]['search_result'], {'name': 'Found User', 'email': 'found@test.com'})

if __name__ == '__main__':
    unittest.main()
