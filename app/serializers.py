from rest_framework import serializers
from .models import Questions
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer,HyperlinkedIdentityField


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    Image = serializers.ImageField(use_url=True)
    class Meta:
       model= Questions
       fields = ['url','id','Text','Image','Tags']