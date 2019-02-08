from django.test import TestCase, Client
from garden_project.factories import UserFactory, TemperatureFactory, SoilMoistureFactory


class TestGardenViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('secret')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'class="login-form container"', res.content)

    def test_view_list_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        temp = TemperatureFactory(user=self.user)
        soil = SoilMoistureFactory()
        res = self.c.get('')

        self.assertIn(temp.temperature.encode(), res.content)
        self.assertEqual(soil.has_moisture, True)

    def test_view_weekly_views(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        temp = TemperatureFactory(user=self.user)
        soil = SoilMoistureFactory()
        res = self.c.get('/raspberry/weekly')

        self.assertIn(temp.temperature.encode(), res.content)
        self.assertEqual(soil.has_moisture, True)


    def test_view_monthly_views(self):
        self.c.login(
            username=self.user.username,
            password='secret'
        )

        temp = TemperatureFactory(user=self.user)
        soil = SoilMoistureFactory()
        res = self.c.get('/raspberry/monthly')

        self.assertIn(temp.temperature.encode(), res.content)
        self.assertEqual(soil.has_moisture, True)
