from django.shortcuts import render
from doctor.models import Doctor

# Create your views here.
def doctor(request):
    doctors = Doctor.objects.all()
    return render(request,"doctor/doctor.html",{"doctors":doctors})
