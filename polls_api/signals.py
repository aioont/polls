from django.db.models.signals import post_save
from django.dispatch import receiver
from polls.models import Question
from .models import PollDetail

@receiver(post_save, sender=Question)
def create_poll_detail(sender, instance, created, **kwargs):
    if created:
        PollDetail.objects.create(poll=instance)
