from django.http import HttpResponse
from django.shortcuts import render

import MyCalendar.Calendar.models


def calendar_index():
    return HttpResponse(MyCalendar.Calendar.models.CalendarClass)
