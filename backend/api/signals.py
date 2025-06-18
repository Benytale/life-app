from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Video

@receiver(post_save, sender=Video)
def handle_video_upload(sender, instance, created, **kwargs):
    if created:
        # Placeholder: trigger analytics or ad-integration pipeline
        pass
