# pylint: disable=W0613
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Triggered by User model to create profile for every new user
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        Profile.objects.create(user=instance) # pylint: disable=E1101


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Triggered by User model to save profile for every new user
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.profile.save()
