from django.db import models


class Contract(models.Model):
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
    name = models.CharField(max_length=30, null=False)
    num1 = models.IntegerField()
    service1 = models.CharField(max_length=500, null=False)
    description1 = models.TextField(max_length=500, null=False)
    categories1 = models.CharField(max_length=20, choices=CATEGORYS)

    num2 = models.IntegerField()
    service2 = models.CharField(max_length=500, null=False)
    description2 = models.TextField(max_length=500, null=False)
    categories2 = models.CharField(max_length=20, choices=CATEGORYS)

    num3 = models.IntegerField()
    service3 = models.CharField(max_length=500, null=False)
    description3 = models.TextField(max_length=500, null=False)
    categories3 = models.CharField(max_length=20, choices=CATEGORYS)

    num4 = models.IntegerField()
    service4 = models.CharField(max_length=500, null=False)
    description4 = models.TextField(max_length=500, null=False)
    categories4 = models.CharField(max_length=20, choices=CATEGORYS)

    num5 = models.IntegerField()
    service5 = models.CharField(max_length=500, null=False)
    description5 = models.TextField(max_length=500, null=False)
    categories5 = models.CharField(max_length=20, choices=CATEGORYS)

    num6 = models.IntegerField()
    service6 = models.CharField(max_length=500, null=False)
    description6 = models.TextField(max_length=500, null=False)
    categories6 = models.CharField(max_length=20, choices=CATEGORYS)

    num7 = models.IntegerField()
    service7 = models.CharField(max_length=500, null=False)
    description7 = models.TextField(max_length=500, null=False)
    categories7 = models.CharField(max_length=20, choices=CATEGORYS)

    num8 = models.IntegerField()
    service8 = models.CharField(max_length=500, null=False)
    description8 = models.TextField(max_length=500, null=False)
    categories8 = models.CharField(max_length=20, choices=CATEGORYS)

    num9 = models.IntegerField()
    service9 = models.CharField(max_length=500, null=False)
    description9 = models.TextField(max_length=500, null=False)
    categories9 = models.CharField(max_length=20, choices=CATEGORYS)

    num10 = models.IntegerField()
    service10 = models.CharField(max_length=500, null=False)
    description10 = models.TextField(max_length=500, null=False)
    categories10 = models.CharField(max_length=20, choices=CATEGORYS)

    def __str__(self):
        return str(self.name)
