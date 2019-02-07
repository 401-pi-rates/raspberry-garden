from django.test import TestCase, RequestFactory
from .models import Temperature
from django.contrib.auth.models import User
from django.utils import timezone

class TestTempModel(TestCase):
    """ This is a class based test which allows for the build up
    and tear down of a test database  """

    def test_alive(self):
        self.assertEqual(True, True)

    def test_has_user(self):
        user = User(username="tester", email="test@test", password="testword")
        self.assertIsInstance(user, User)

    def test_has_temp(self):
        # user = User(username="tester", email="test@test", password="testword")
        temp = Temperature(temperature=99)
        self.assertEqual(temp.temperature, 99)

    def test_has_date(self):
        now = timezone.now()
        time = Temperature(date_added=now)
        self.assertEqual(time.date_added, now)


