from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile

# signal listening for when an instance of User is saved
# post_save decorator produces created bool used in func to check if a profile needs to be created 
# __init__.py and apps.py need code for this to work 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)