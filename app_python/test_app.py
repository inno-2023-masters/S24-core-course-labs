import unittest
import datetime
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_moscow_time_calculation(self):
        utc_now = datetime.datetime.utcnow()
        expected_moscow_time = utc_now + datetime.timedelta(hours=3)
        expected_time_str = expected_moscow_time.strftime("%Y-%m-%d %H:%M:%S")
        response = self.app.get('/')
        displayed_time_str = response.data.decode('utf-8').split(': ')[1].split('</h1>')[0].strip()
        self.assertEqual(displayed_time_str, expected_time_str)

if __name__ == '__main__':
    unittest.main()
