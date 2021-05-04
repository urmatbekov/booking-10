from django.shortcuts import render
from django.http import HttpResponse
from client.models import Client

# Create your views here.
def client(request):
    clients = Client.objects.all()
    results = "<ul>"
    for cl in clients:
        results += "<li>{} {} {}</li> ".format(cl.name,cl.surname,cl.age)
    results += "</ul>"
    return HttpResponse(results)