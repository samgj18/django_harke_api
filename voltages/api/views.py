'''Views API'''

# Python
from datetime import date

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated


# Models
from voltages.models import UserData, Testing, VerifyTesting

# Serializers
from voltages.api.serializers import DataSerializer, DataTestingSerializer, DataVerifyTestingSerializer


class DataViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    '''DataViewSet ModelViewSet

        Determines or contains the logic for handling the model
        and show all the data. Accepts for lookups with ?q= format only
        for the activity'''
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        '''Redefining the get_serializer method for accepting a list of
            dicts'''
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(DataViewSet, self).get_serializer(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):  # pylint: disable=arguments-differ,unused-argument
        '''Redefining the get_queryset method for accepting activity params
            through the URL'''
        queryset_list = UserData.objects.all()  # pylint: disable=no-member
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(activity__icontains=query)
            ).distinct()
        return queryset_list


class DataTestViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    '''DataViewSet ModelViewSet

        Determines or contains the logic for handling the model for
        showing all the training data'''
    queryset = Testing.objects.all()  # pylint: disable=no-member
    serializer_class = DataTestingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        '''Redefining the get_serializer method for accepting a list of
            dicts'''
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(DataTestViewSet, self).get_serializer(*args, **kwargs)


class DataViewSingleUser(ModelViewSet):  # pylint: disable=too-many-ancestors
    '''DataViewSet ModelViewSet

        Determines or contains the logic for handling the model and showing
        only the user info'''
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):  # pylint: disable=arguments-differ,unused-argument
        '''Redefining the get_queryset method for accepting date params
            through the URL'''
        queryset_list = UserData.objects.all().filter(  # pylint: disable=no-member
            user=self.request.user)  # pylint: disable=no-member
        dates = self.request.GET.get('q')
        if dates:
            dates = dates.split('-')
            date_2_complete = dates[1].split(',')
            date_1_complete = dates[0].split(',')
            date_1 = int(date_1_complete[0])
            date_2 = int(date_1_complete[1])
            date_3 = int(date_1_complete[2])
            date_4 = int(date_2_complete[0])
            date_5 = int(date_2_complete[1])
            date_6 = int(date_2_complete[2])
            queryset_list = UserData.objects.filter(user=self.request.user).filter(  # pylint: disable=no-member
                created__range=(date(date_1, date_2, date_3), date(date_4, date_5, date_6))).all()
        return queryset_list


class DataVerifyTestViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    '''DataViewSet ModelViewSet

        Determines or contains the logic for handling the model for
        showing all the testing data'''
    queryset = VerifyTesting.objects.all()  # pylint: disable=no-member
    serializer_class = DataVerifyTestingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        '''Redefining the get_serializer method for accepting a list of
            dicts'''
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(DataVerifyTestViewSet, self).get_serializer(*args, **kwargs)
