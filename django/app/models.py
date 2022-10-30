from django.db import models
import uuid
# Create your models here.

class Event(models.Model):
    name=  models.TextField()
    uuid= models.UUIDField(default=uuid.uuid4, editable=False)
    source= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True)
    description= models.TextField()

    def __str__(self):
        return self.name + ' ' + self.description

