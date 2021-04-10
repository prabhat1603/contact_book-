from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal
from contactapp.models import ContactBook
from django.contrib import messages


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ContactBook.objects.create(name = instance)
    print(f"Default Profile for {instance.username} is created!")
