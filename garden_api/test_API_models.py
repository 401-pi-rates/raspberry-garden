from django.test import TestCase  #RequestFactory
from .models import SoilMoisture
# from django.contrib.auth.models import User
from django.utils import timezone


class TestMoistureModel(TestCase):
    """ This is a class based test which allows for the build up
    and tear down of a test database  """

    def test_alive(self):
        self.assertEqual(True, True)

    def test_has_moisture(self):
        # user = User(username="tester", email="test@test", password="testword")
        moist = SoilMoisture(has_moisture="yes")
        self.assertEqual(moist.has_moisture, "yes")

    def test_has_date(self):
        now = timezone.now()
        time = SoilMoisture(time_stamp=now)
        self.assertEqual(time.time_stamp, now)

