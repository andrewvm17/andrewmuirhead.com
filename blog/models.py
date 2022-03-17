from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.RichTextField(config_name = "default")
    date_posted = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)



def __str__(self): 
    return self.title
