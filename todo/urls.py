from django.urls import path, include
from rest_framework import routers, urlpatterns
from . import views

router = routers.DefaultRouter()
router.register(r'Todo', views.ToDoViewSets)

urlpatterns = [
    path('', include(router.urls))
]
