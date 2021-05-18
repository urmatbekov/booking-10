from django.db import models



class Profes(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

# Create your models here.
class Doctor(models.Model):
    name = models.CharField("Имя",max_length=120)
    surname = models.CharField("Фамилия",max_length=120)
    age = models.IntegerField("Возраст")
    photo = models.ImageField("Фото",upload_to="doctor/",null=True)
    profes = models.ForeignKey(Profes,null=True,on_delete=models.CASCADE)
    

    def __str__(self):
        return "{} {} - {}".format(self.name,self.surname,self.profes)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Докторы"