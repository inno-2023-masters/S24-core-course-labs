import unittest
from app import get_moscow_time
from datetime import datetime
import pytz


class TestApp(unittest.TestCase):

    def test_get_moscow_time(self):
        # Call the get_moscow_time function
        result = get_moscow_time()

        moscow_timezone = pytz.timezone('Europe/Moscow')
        expected_result = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
