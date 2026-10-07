from django.db import models


class usersinfo(models.Model):
    photo=models.ImageField()
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=50)


# Create your models here.
class doctorsinfo(models.Model):
    docphoto=models.ImageField()
    docname=models.CharField(max_length=50)
    docspecialization=models.CharField(max_length=50)
    docpayment=models.FloatField(max_length=50)
    doctiming=models.CharField(max_length=50)

class appointmentsinfo(models.Model):
    userid=models.CharField(max_length=12)
    patientname=models.CharField(max_length=200)
    patientage=models.IntegerField(max_length=200)
    patientemail=models.CharField(max_length=200)
    patientphone=models.IntegerField(max_length=200)
    docname=models.CharField(max_length=200)
    bookingdate=models.CharField(max_length=200)
    patientproblem=models.CharField(max_length=200)