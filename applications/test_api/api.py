from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .serializers import *


class ResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = ResultsSetPagination


class PetViewSet(ReadOnlyModelViewSet):
    queryset = Pet.objects
    serializer_class = PetSerializer

    @action(methods=['GET'], detail=False)
    def have_friends(self, request):
        queryset = self.get_queryset().have_friends(True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def have_not_friends(self, request):
        queryset = self.get_queryset().have_friends(False)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


