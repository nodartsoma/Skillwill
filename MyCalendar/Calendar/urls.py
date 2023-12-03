from django.urls import path

from MyCalendar.Calendar import views

urlpatterns = [
    path('/api/Calendar', views.calendar_index())
]
