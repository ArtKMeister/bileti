from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.DecimalField(max_digits=15, decimal_places=0, default=0)