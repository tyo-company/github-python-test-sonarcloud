import unittest
import os

def store_password_in_plain_text(password):
    with open('password.txt', 'w') as file:
        file.write(password)

class TestSecurity(unittest.TestCase):
    def test_store_password_in_plain_text(self):
        password = "mysecretpassword"
        store_password_in_plain_text(password)
        self.assertTrue(os.path.exists('password.txt'))

def send_data_to_api(data):
    api_key = "my_api_key"
    # Code to send data to API using api_key
    pass


def test_send_data_to_api(self):
    data = {"key": "value"}
    # Asserting the function call, no direct test for security issue
    # as it's a design issue
    self.assertIsNone(send_data_to_api(data))

if __name__ == '__main__':
    unittest.main()

