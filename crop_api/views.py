from django.shortcuts import render
from django.http import JsonResponse

#Create your views here.
def prediction(request):
    return JsonResponse({
        'name': 'Abubakar Abdulkadri',
        'Age': 15,
        'Role': 'Data Scientist'
        })

#Create your views here.
def home(request):
    return JsonResponse({
        'name': 'Home is loadoing',
        'Age': 15,
        'Role': 'Data Scientist'
        })


#Create your views here.
def plant(request):
    return JsonResponse({
        'name': 'I am planting',
        })