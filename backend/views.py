from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    manage = 'Successed'
    return JsonResponse(manage,safe=False)