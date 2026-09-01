from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name
    
