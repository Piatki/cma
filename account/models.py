from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    POSITIONS = [
        ("Страховой агент", "Страховой агент"),
        ("Консультант", "Консультант"),
        ("Охранник", "Охранник")
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True, choices=POSITIONS)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
