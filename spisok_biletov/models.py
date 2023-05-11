from django.db import models

# Create your models here.


class SpisokBiletov(models.Model):
    name = models.CharField(max_length=256)
    name_out = models.CharField(max_length=256)
    name_in = models.CharField(max_length=256)
    date = models.DateField()
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=512)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)


