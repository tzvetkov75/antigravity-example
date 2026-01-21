# Audo added TEXT-123
import sys
from unittest.mock import MagicMock

# Mock mysql.connector if not installed or validation fails
try:
    import mysql.connector
except ImportError:
    # Creative mocking to allow import of users_db
    mock_mysql = MagicMock()
    sys.modules['mysql'] = mock_mysql
    sys.modules['mysql.connector'] = mock_mysql

import unittest
from unittest.mock import patch
# Import users_db after mocking
import users_db

class TestDatabaseOperations(unittest.TestCase):
    
    def setUp(self):
        # Ensure we can patch mysql.connector even if satisfied by our mock
        if 'mysql.connector' not in sys.modules:
             sys.modules['mysql.connector'] = MagicMock()

    @patch('users_db.mysql.connector.connect')
    @patch.dict('os.environ', {
        'DB_HOST': 'localhost',
        'DB_USER': 'user',
        'DB_PASSWORD': 'password',
        'DB_NAME': 'test_db'
    })
    def test_get_db_connection(self, mock_connect):
        """Test database connection is established with correct env vars."""
        users_db.get_db_connection()
        mock_connect.assert_called_with(
            host='localhost',
            user='user',
            password='password',
            database='test_db'
        )

    def test_create_users_table(self):
        """Test SQL query for creating users table."""
        mock_cursor = MagicMock()
        users_db.create_users_table(mock_cursor)
        
        # Verify the execute call contains expected SQL parts
        args, _ = mock_cursor.execute.call_args
        sql = args[0]
        self.assertIn("CREATE TABLE IF NOT EXISTS users_table", sql)
        self.assertIn("name VARCHAR(255) NOT NULL", sql)
        self.assertIn("email VARCHAR(255) NOT NULL UNIQUE", sql)
        self.assertIn("password VARCHAR(255) NOT NULL", sql)

    def test_add_user(self):
        """Test SQL query for adding a user."""
        mock_cursor = MagicMock()
        users_db.add_user(mock_cursor, "Test User", "test@example.com", "secret")
        
        expected_query = "INSERT INTO users_table (name, email, password) VALUES (%s, %s, %s)"
        expected_values = ("Test User", "test@example.com", "secret")
        
        mock_cursor.execute.assert_called_with(expected_query, expected_values)

if __name__ == '__main__':
    unittest.main()
