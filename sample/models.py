from django.db import models


# Create your models here.
class SampleModel(models.Model):
    user_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
