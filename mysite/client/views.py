from django.shortcuts import render
from client.models import Client

# Create your views here.
def client(request):
    clients = Client.objects.all()
    
    return render(request,"client/client.html",{"clients":clients})