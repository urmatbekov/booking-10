from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField("Имя",max_length=120)
    surname = models.CharField("Фамилия",max_length=120)
    age = models.IntegerField("Возраст")
    photo = models.ImageField("Фото",upload_to="doctor/",null=True)
    

    def __str__(self):
        return "{} {}".format(self.name,self.surname)

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Докторы"