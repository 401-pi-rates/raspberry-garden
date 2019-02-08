import factory
from django.contrib.auth.models import User
from garden_api.models import SoilMoisture
from garden_app.models import Temperature


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class TemperatureFactory(factory.django.DjangoModelFactory):
    """Create a test category for writing tests."""

    class Meta:
        model = Temperature

    # has_moisture = factory.SubFactory(SoilMoisture)
    user = factory.SubFactory(UserFactory)
    temperature = factory.Faker('postalcode')


class SoilMoistureFactory(factory.django.DjangoModelFactory):
    """
    """
    class Meta:
        model = SoilMoisture

    has_moisture = True
