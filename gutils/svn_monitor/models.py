from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    date = models.DateTimeField(default=timezone.now)

class Tag_Value(models.Model):
    tag_id = models.ForeignKey(Tag,on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def get_value(token):
        tag, locale = token.split('@', 1)
        try:
            return Tag_Value.objects.get(tag_id=tag, locale=locale).value
        except (ValueError, Tag_Value.DoesNotExist):
            return '[['+token+']]'