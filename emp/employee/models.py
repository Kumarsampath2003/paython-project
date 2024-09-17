from django.db import models

class employee(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)

