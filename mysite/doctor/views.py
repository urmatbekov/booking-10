from django.http.response import HttpResponse
from django.shortcuts import render
from doctor.models import Doctor

# Create your views here.
def doctor(request):
    doctors = Doctor.objects.all()
    return render(request,"doctor/doctor.html",{"doctors":doctors})

def doctor_detail(request,id):
    doctor = Doctor.objects.get(id=id)
    return render(request,"doctor/detail.html",{"doctor":doctor})
