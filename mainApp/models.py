from django.db import models

# Create your models here.
class Number(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)
