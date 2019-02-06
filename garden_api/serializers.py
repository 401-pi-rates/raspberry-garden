"""This module contains serializer to be used for api views."""
from django.contrib.auth.models import User
from garden_app.models import Temperature, WaterLevel
from rest_framework import serializers
from .models import SoilMoisture


class UserSerializer(serializers.ModelSerializer):
    """To serialize the fields in User model."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user


class SoilMoistureSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        """
        """
        model = SoilMoisture
        fields = ('has_moisture', 'time_stamp')


# class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
#     """To serialize the fields in Temperature model."""
#     # owner is the user name in database:
#     owner = serializers.ReadOnlyField(source='user.username')

#     # user will be something like "http://localhost:8000/api/v1/user/1":
#     user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

#     class Meta:
#         model = Temperature
#         fields = ('owner', 'user', 'temperature', 'date_added')


# class WaterLevelSerializer(serializers.HyperlinkedModelSerializer):
#     """To serialize the fields in WaterLevel model."""
#     owner = serializers.ReadOnlyField(source='user.username')

#     user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

#     class Meta:
#         model = WaterLevel
#         fields = ('owner', 'user', 'water', 'date_added')
