from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    concern = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email

class Buyticket(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender1 = models.CharField(max_length=10)
    stop01 = models.CharField(max_length=10)
    stop02 = models.CharField(max_length=10)


    def __str__(self):
        return self.name + " - " + self.email

class Buypass(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender2 = models.CharField(max_length=10)
    durationtype = models.CharField(max_length=10)
  

    def __str__(self):
        return self.name + " - " + self.email

