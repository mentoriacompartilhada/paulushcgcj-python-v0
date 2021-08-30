from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=40)
