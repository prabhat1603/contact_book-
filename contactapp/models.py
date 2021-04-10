from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models

# Create your models here.

class ContactBook(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    phone = models.BigIntegerField(blank = True, null = True)
    profession = models.TextField()
    address = models.TextField()
    profile = models.ImageField(upload_to = "profile", default = "default.jpg")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
       return reverse('contactapp:contactdetail', kwargs={'pk' : self.pk})
