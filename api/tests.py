
from rest_framework.test import APITestCase


class APITest(APITestCase):

    def test_get_data_logged_in(self):
        response = self.client.get('http://127.0.0.1:8000/api/bileti/main')
        print(response.data)
# Create your tests here.
