# Audo added TEXT-123
# Copyright (c) 2026. All rights reserved.
# Licensed under the MIT License.

import unittest
from unittest.mock import MagicMock, patch
import database_operations

class TestDatabaseOperations(unittest.TestCase):
    @patch('mysql.connector.connect')
    def test_get_db_connection_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_conn.is_connected.return_value = True
        mock_connect.return_value = mock_conn
        
        conn = database_operations.get_db_connection()
        self.assertIsNotNone(conn)
        self.assertTrue(conn.is_connected())

    @patch('mysql.connector.connect')
    def test_get_db_connection_failure(self, mock_connect):
        mock_connect.side_effect = database_operations.Error("Connection failed")
        
        conn = database_operations.get_db_connection()
        self.assertIsNone(conn)

    def test_create_table(self):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        database_operations.create_table_if_not_exists(mock_conn)
        
        mock_cursor.execute.assert_called_once()
        self.assertIn("CREATE TABLE IF NOT EXISTS users_table", mock_cursor.execute.call_args[0][0])
        mock_conn.commit.assert_called_once()

    def test_add_user(self):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        
        database_operations.add_user(mock_conn, "Test User", "test@example.com", "password")
        
        mock_cursor.execute.assert_called_once()
        self.assertIn("INSERT INTO users_table", mock_cursor.execute.call_args[0][0])
        self.assertEqual(mock_cursor.execute.call_args[0][1], ("Test User", "test@example.com", "password"))
        mock_conn.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
