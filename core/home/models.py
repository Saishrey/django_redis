from django.db import models

# Create your models here.
class Fruits(models.Model):
    fruit_name = models.CharField(max_length=100)

    def __str__(self):
        return self.fruit_name