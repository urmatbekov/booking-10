from django.shortcuts import render
from client.models import Client

# Create your views here.
def client(request):
    clients = Client.objects.all()
    results = "<ul>"
    for cl in clients:
        results += "<li>{} {} {}</li> ".format(cl.name,cl.surname,cl.age)
    results += "</ul>"
    return render(request,"client/client.html")