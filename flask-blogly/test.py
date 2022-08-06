from unittest import TestCase
from app import app, check_amount, handle_submit

class ConverterTests(TestCase):

    def test_html(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>User list</h1>', html)

    def i_hate_tests(self):
        with app.test_client() as client:
            res = client.post('/1')
            html = res.get_data(as_text=True)
            self.assertIn('<h1>Yui Details</h1>', html)

    def nobody_likes_tests(self):
        with app.test_client() as client:
            res = client.post('/1/edit_user')
            html = res.get_data(as_text=True)
            self.assertIn('<h1>Profile Settings</h1>', html)

    def lets_waste_more_time_with_tests(self):
        with app.test_client() as client:
            res = client.post('/AddUser')
            html = res.get_data(as_text=True)
            self.assertIn('<h1>Add a new user</h1>', html)



