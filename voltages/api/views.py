from rest_framework import viewsets
from voltages.models import UserData, Testing
from voltages.api.serializers import DataSerializer, DataTestingSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

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

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


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

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class DataViewSingleUser(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set


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