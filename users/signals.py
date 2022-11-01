from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

# создаем
@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)

# обновлем
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()