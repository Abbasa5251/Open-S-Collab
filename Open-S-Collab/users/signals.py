from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        porfile = Profile.objects.create(
            user=user, username=user.username, email=user.email, name=user.first_name
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
