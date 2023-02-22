from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile_user')
    date_created = models.DateTimeField(auto_now_add=True)
    tel = models.IntegerField(default=0, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    street = models.CharField(max_length=100, blank=True)
    addr_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user.email)


class Product(models.Model):
    name = models.TextField()
    category = models.TextField()
    description = models.TextField()
    prize = models.FloatField()
    promotion = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ' ' + str(self.prize) + ' ' + str(self.promotion)
