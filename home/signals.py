from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

@receiver(pre_save, sender=User)
def validate_unique_email_and_normalize(sender, instance, **kwargs):
    if instance.email:
        normalized_email = instance.email.strip().lower()
        instance.email = normalized_email
        qs = User.objects.filter(email__iexact=normalized_email)
        if instance.pk:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise ValidationError(f"A user with the email '{normalized_email}' already exists.")

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
            instance.save(update_fields=['password'])
