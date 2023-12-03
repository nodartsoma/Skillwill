from django.http import HttpResponse
from django.shortcuts import render

import MyCalendar.User.models


def user_index():
    return HttpResponse(MyCalendar.User.models.UserClass)
