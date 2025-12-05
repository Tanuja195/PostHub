from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
        # Profile.objects.get(user=instance) this is another way writing the instance of Profile instance


from django.core.signals import request_started, request_finished
from django.dispatch import receiver
from datetime import datetime
# from ipware import get_client_ip
# from django.urls import 

@receiver(request_started)
def log_request(sender, **kwargs):
    print(f"Request started at {datetime.now()}")
    
@receiver(request_finished)
def log_request2(sender, **kwargs):
    print(f"Request finished at {datetime.now()}")


from django.core.mail import send_mail
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()