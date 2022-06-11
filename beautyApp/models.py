from django.db import models


class Services(models.Model):
    services_title = models.CharField(max_length=200)
    services_duration = models.IntegerField()
    services_price = models.IntegerField()
    image = models.ImageField()
