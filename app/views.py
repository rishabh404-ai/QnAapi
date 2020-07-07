from django.shortcuts import render
from rest_framework import viewsets
from .models import Questions
from .serializers import QuestionsSerializer
from django_filters import FilterSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    filter_backends = (OrderingFilter,SearchFilter)
    search_fields = ('Tags',)
    ordering_fields = ('id',)
       