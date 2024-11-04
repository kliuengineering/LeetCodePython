import unittest


############## Simple Unit Test ##############

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()


############## Simple Mocks ##############
"""
Mocks: simulate objects or functions during testing, 
especially when dealing with dependencies like databases, 
APIs, or external services. 
In Python, unittest.mock provides tools for creating mocks.
"""

from unittest import TestCase
from unittest.mock import Mock, patch

# Function we want to test
def get_user_name(user_id, db):
    return db.get_name(user_id)

class TestGetUserName(TestCase):
    @patch("db_module.Database")  # Mock the Database class in db_module
    def test_get_user_name(self, MockDatabase):
        # Set up the mock database
        mock_db = MockDatabase()
        mock_db.get_name.return_value = "Alice"

        # Test the function
        user_name = get_user_name(1, mock_db)
        self.assertEqual(user_name, "Alice")
        mock_db.get_name.assert_called_once_with(1)  # Verify interaction


############## Simple Fake #################################
"""
A fake is a simplified implementation of a 
dependency that has some functionality. 

Heres a fake database class to test 
functions that require a database connection.
"""
class FakeDatabase:
    def __init__(self):
        self.users = {1: "Alice", 2: "Bob"}

    def get_name(self, user_id):
        return self.users.get(user_id, "Unknown")

def get_user_name(user_id, db):
    return db.get_name(user_id)

class TestGetUserNameWithFake(TestCase):
    def test_get_user_name_with_fake(self):
        fake_db = FakeDatabase()
        self.assertEqual(get_user_name(1, fake_db), "Alice")
        self.assertEqual(get_user_name(3, fake_db), "Unknown")


############## Simple Fake #########################
"""
A stub provides minimal behavior required for the test, 
often returning a fixed value. Unlike a fake, 
it doesnt contain full functionality.
"""
class StubService:
    def send_email(self, user_id, message):
        return True  # Stubbed to always succeed

def notify_user(user_id, service):
    if service.send_email(user_id, "Welcome!"):
        return "Notification sent"
    return "Notification failed"

class TestNotifyUser(TestCase):
    def test_notify_user_with_stub(self):
        stub_service = StubService()
        self.assertEqual(notify_user(1, stub_service), "Notification sent")

