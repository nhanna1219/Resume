from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile

@receiver(post_save, sender=User)
def create_Profile(sender, instance, created, **kwargs):
    """Hàm được gọi đến khi một đối tượng User được tạo và lưu,
        nếu created == true thì UserProfile sẽ được tạo kết với 
        User model có sẵn trong hệ thống"""
    if created:
        userprofile = UserProfile.objects.create(user=instance)