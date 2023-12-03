from django.urls import path

from MyCalendar.User import views

urlpatterns = [
    path('/api/User', views.user_index())
]
