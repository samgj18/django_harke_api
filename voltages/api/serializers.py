'''Serializers API'''

# Django
from django.contrib.auth.models import User
from rest_auth.models import TokenModel

# Django REST Framework
from rest_framework import serializers

# Models
from voltages.models import UserData, Testing, VerifyTesting


class DataSerializer(serializers.ModelSerializer):
    ''' Serializer of all the data from all users'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta content of the serializer'''
        model = UserData
        fields = ('user', 'voltage_coil_1', 'voltage_coil_2',
                  'voltage_generated_by_user', 'activity', 'datetime')


class DataTestingSerializer(serializers.ModelSerializer):
    ''' Serializer of all the data from all users without user tag, 
    for training purposes'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta content of the serializer'''
        model = Testing
        fields = ('voltage_coil_1', 'voltage_coil_2',
                  'voltage_generated_by_user', 'activity')


class DataVerifyTestingSerializer(serializers.ModelSerializer):
    ''' Serializer of all the data, for testing purposes'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta content of the serializer'''
        model = VerifyTesting
        fields = ('user', 'detected_activity',
                  'real_activity', 'datetime')


class UserSerializer(serializers.ModelSerializer):
    ''' Serializer that returns more info needed in the login'''
    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta content of the serializer'''
        model = User
        fields = ('id', 'email')


class TokenSerializer(serializers.ModelSerializer):
    ''' Serializer that returns more info needed in the login auxiliar'''
    user = UserSerializer()

    class Meta:  # pylint: disable=too-few-public-methods
        '''Meta content of the serializer'''
        model = TokenModel
        fields = ('key', 'user')
