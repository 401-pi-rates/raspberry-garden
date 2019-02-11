"""This module contains views based on rest framework."""
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .serializers import UserSerializer, SoilMoistureSerializer, User, SoilMoisture


class RegisterApiView(generics.CreateAPIView):
    """To set up register api view."""
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    """To set up user api view."""
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class SoilMoistureApiView(generics.CreateAPIView):
    """
    API view for the input RPi data.
    """
    serializer_class = SoilMoistureSerializer


class SoilMoistureDetailApiView(generics.RetrieveAPIView):
    """
    API view for the input RPi data.  Used to test and validate the endpoint for the RPi.
    """
    serializer_class = SoilMoistureSerializer

    def get_queryset(self):
        return SoilMoisture.objects.filter()

# class CurrentApiView(generics.ListCreateAPIView):
#     """To set up current api view."""
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = WaterLevelSerializer

#     # How to get only the most recent entry from db?

#     def get_queryset(self):
#         return WaterLevel.objects.filter(
#             user__username=self.request.user.username)

#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user.id)


# class WeeklyApiView(generics.ListCreateAPIView):
#     """To set up weekly-trend api view."""
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = WaterLevelSerializer

#     # How to get only the entries for the past 7 days?

#     def get_queryset(self):
#         return WaterLevel.objects.filter(
#             user__username=self.request.user.username)

#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user.id)


# class MonthlyApiView(generics.ListCreateAPIView):
#     """To set up weekly-trend api view."""
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = WaterLevelSerializer

#     # How to get only the entries for the past 30 days?

#     def get_queryset(self):
#         return WaterLevel.objects.filter(
#             user__username=self.request.user.username)

#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user.id)
