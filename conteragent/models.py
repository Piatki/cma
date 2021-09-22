from django.db import models
from django.utils import timezone


class LPU(models.Model):
    CATEGORYS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11')
    )
    name = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=40, null=False)
    category = models.CharField(max_length=2, choices=CATEGORYS)

    def __str__(self):
        return str(self.name)


