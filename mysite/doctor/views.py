from django.shortcuts import render
from doctor.models import Doctor
from django.http import HttpResponse

# Create your views here.
def doctor(request):
    doctors = Doctor.objects.all()
    return HttpResponse("Hello doctor")
