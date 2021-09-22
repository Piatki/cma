from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ClientAppeal(models.Model):
    TASKS = (
        ('скорая помощь', 'скорая помощь'),
        ('амбулаторная помощь', 'амбулаторная помощь'),
        ('стоматология', 'стоматология'),
        ('прогарантировать', 'прогарантировать')
    )
    lpu = models.ForeignKey('conteragent.Lpu', on_delete=models.CASCADE)
    date_create = models.DateField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.TextField(max_length=5000)
    task = models.CharField(max_length=20, choices=TASKS)
    diagnoz = models.TextField(max_length=1500)

    def __str__(self):
        return str(self.diagnoz)


class MKB(models.Model):
    name_mkb = models.CharField(max_length=200)

