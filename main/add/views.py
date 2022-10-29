from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from add.models import Putin_order
from add.serializers import PutinOrderSerializer


class SearchList(generics.ListAPIView):
    """
    Представление нашей базы данных через API
    """
    queryset = Putin_order.objects.all()
    serializer_class = PutinOrderSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['chapter_name']
