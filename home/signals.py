from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.ensure_qr_token()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.ensure_qr_token()
        instance.profile.save()


@receiver(post_save, sender=User)
def ensure_hashed_password(sender, instance, created, **kwargs):
    if created and instance.password:
        from django.contrib.auth.hashers import make_password
        if not instance.password.startswith('pbkdf2_'):
            instance.password = make_password(instance.password)
            instance.save()
