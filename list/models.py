from django.db import models

# Create your models here.

class Url(models.Model):
    id  = models.IntegerField(primary_key=True)
    original_url = models.CharField(max_length=150,null=False)
    short_url = models.CharField(max_length=100,null=False)
    created_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    