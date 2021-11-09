from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _



class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(max_length=720, default='')
    mobile = models.CharField(max_length=16, default="")
    image = models.ImageField(upload_to='profiles/', null=True, blank=True ,default='')
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    specialty = models.ManyToManyField(
        "specialty", verbose_name=_('تخصص ها'), related_name="specialty")

    def __str__(self):
        return self.user.username


# Create User --> Create Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class specialty (models.Model):
    title = models.CharField(_("عنوان نمایشی"),max_length=255)
    slug = models.CharField(_("عنوان لاتین"), max_length=255)
    publish = models.DateTimeField(
        _('تاریخ انتشار'), auto_now_add=True, auto_now=False)
    update = models.DateTimeField(
        _('تاریخ بروزرسانی'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.slug