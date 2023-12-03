from django.urls import path

from . import views

urlpatterns = [
    path('/api/Calendar', views.calendar_index)
]
