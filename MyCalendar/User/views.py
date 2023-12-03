from django.http import HttpResponse
from django.shortcuts import render


def user_index():
    return HttpResponse('It worked!! God damnit')
