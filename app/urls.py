from django.urls import path,include
from . import views
from rest_framework import routers
from .models import Questions

router = routers.DefaultRouter()
router.register('Questions',views.QuestionsViewSet)
urlpatterns = [
    path('', include(router.urls))  
]