from django.test import TestCase


class BiletiViewTest(TestCase):

    def test_index_load(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_datapoisk_load(self):
        response = self.client.get('http://127.0.0.1:8000/datapoisk/')
        self.assertEqual(response.status_code, 200)

    def test_gorodpoisk_load(self):
        response = self.client.get('http://127.0.0.1:8000/gorodpoisk/')
        self.assertEqual(response.status_code, 200)
