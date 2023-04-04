from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    carousel_caption_title = models.CharField(max_length=30)
    carousel_caption_description =  models.CharField(max_length=80)
    heading = models.CharField(max_length=15)
    description = models.CharField(max_length=120)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")

    def __str__(self):
        return f"{self.id} -- {self.heading} -- {self.description}"
