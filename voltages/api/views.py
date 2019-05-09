from rest_framework import viewsets
from voltages.models import UserData, Testing
from voltages.api.serializers import DataSerializer, DataTestingSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from datetime import date


class DataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(DataViewSet, self).get_serializer(*args, **kwargs)


class DataTestViewSet(viewsets.ModelViewSet):

    queryset = Testing.objects.all()
    serializer_class = DataTestingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(DataTestViewSet, self).get_serializer(*args, **kwargs)


class DataViewSingleUser(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset_list = UserData.objects.all().filter(user=self.request.user)
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
            queryset_list = UserData.objects.filter(user=self.request.user).filter(
                created__range=(date(date_1, date_2, date_3), date(date_4, date_5, date_6))).all()
        return queryset_list


class DataViewSingleActivity(viewsets.ModelViewSet):

    serializer_class = DataTestingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset_list = Testing.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(activity__icontains=query)
            ).distinct()
        return queryset_list
