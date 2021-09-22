from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100, null=False)
    date_birthday = models.DateField(null=False)
    company = models.CharField(max_length=100, null=False)
    program = models.ForeignKey('contractbase.Contract', on_delete=models.CASCADE)
    police_num = models.CharField(max_length=20, null=False)
    date_start_police = models.DateField(null=False)
    date_finish_police = models.DateField(null=False)
    mail = models.EmailField()
    phone_number = models.CharField(max_length=20, null=False)

    def __str__(self):
        return str(self.name)


class ClientCase(models.Model):
    num_case = models.IntegerField()
    date_start_appeal = models.DateTimeField(default=timezone.now())
    date_finish_appeal = models.DurationField()
    status = models.BooleanField()
    mkb_block = models.ForeignKey('clients.MKB', on_delete=models.CASCADE)
    diagnoz = models.ForeignKey('clients.ClientAppeal', on_delete=models.CASCADE)
    coordinator = models.CharField(max_length=2000)



    def __str__(self):
        return str(self.num_case)

