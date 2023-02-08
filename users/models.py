from django.db import models

class User(models.Model):
    name = models.CharField("Name", max_length=240)
    Family_name = models.CharField("Fname", max_length=240)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name