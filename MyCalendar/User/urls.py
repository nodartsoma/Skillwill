from django.urls import path

from . import views

urlpatterns = [
    path('api/User', views.user_index)
]
