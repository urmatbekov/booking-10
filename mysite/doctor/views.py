from django.http.response import HttpResponse
from django.shortcuts import render
from doctor.models import Doctor

# Create your views here.
def doctor(request):
    if request.method == "POST":
        name = request.POST.get("doctor_name")
        surname = request.POST.get("doctor_surname")
        age = request.POST.get("doctor_age")
        if name and surname and age:
            Doctor.objects.create(name=name,surname=surname,age=age)
    doctors = Doctor.objects.all()
    return render(request,"doctor/doctor.html",{"doctors":doctors})

def doctor_detail(request,id):
    doctor = Doctor.objects.get(id=id)
    return render(request,"doctor/detail.html",{"doctor":doctor})
