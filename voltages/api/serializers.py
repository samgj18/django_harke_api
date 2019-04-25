from rest_framework import serializers
from voltages.models import UserData, Testing
from django.contrib.auth.models import User
from rest_auth.models import TokenModel


class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('user', 'voltage_coil_1', 'voltage_coil_2',
                  'voltage_generated_by_user', 'activity', 'datetime')


class DataTestingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = ('voltage_coil_1', 'voltage_coil_2',
                  'voltage_generated_by_user', 'activity')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user')