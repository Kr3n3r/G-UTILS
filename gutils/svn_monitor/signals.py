from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import *

@receiver(post_migrate)
def perform_initial_insertions(sender, **kwargs):
    if sender.name == 'svn_monitor':
        app_version = Tag(id='app.version')
        app_version.save()
        Tag_Value(tag_id=app_version, value='0.1', locale='').save()
