from django.shortcuts import render
from doctor.models import Doctor
from django.http import HttpResponse

# Create your views here.
def doctor(request):
    doctors = Doctor.objects.all()
    result = ""
    for doc in doctors:
        result += "{} {}, ".format(doc.name,doc.surname)
    return HttpResponse(result)
