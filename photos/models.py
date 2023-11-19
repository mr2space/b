from django.db import models
import uuid

def folder_based_option(instance, filename):
    return f"{instance.category}_photo/{filename}"

class Photos(models.Model):
    categoryChoice = [
        (1, 'Self'),
        (0, 'Family'),
        (2, 'Love'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    photo = models.ImageField(upload_to=folder_based_option, null=False, blank=False)
    category = models.IntegerField(default=1,choices=categoryChoice)
    