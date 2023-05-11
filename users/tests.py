from django.test import TestCase
from .models import User
from django.contrib.auth import authenticate

class SigninTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testname',
                                             password='1234test5678',
                                             first_name='Имя',
                                             last_name='Фамилия',
                                             email='test@mail.com',
                                             phone=89999999999,
                                             )
        self.user.save()
    def tearDown(self):
        self.user.delete()
    def test_correct(self):
        user = authenticate(username='testname', password='1234test5678')
        self.assertTrue(user is not None and user.is_authenticated)
    def test_wrong_username(self):
        user = authenticate(username='name', password='1234test5678')
        self.assertFalse(user is not None and user.is_authenticated)
    def test_wrong_pssword(self):
        user = authenticate(username='testname', password='test')
        self.assertFalse(user is not None and user.is_authenticated)
# Create your tests here.
