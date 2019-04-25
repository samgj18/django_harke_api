from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voltage_coil_1 = models.DecimalField(decimal_places=3, max_digits=65)
    voltage_coil_2 = models.DecimalField(decimal_places=3, max_digits=65)
    voltage_generated_by_user = models.DecimalField(
        decimal_places=3, max_digits=65)
    activity = models.IntegerField()
    datetime = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user, self.voltage_coil_1, self.voltage_coil_2, self.voltage_generated_by_user)


class Testing(models.Model):
    voltage_coil_1 = models.DecimalField(decimal_places=3, max_digits=65)
    voltage_coil_2 = models.DecimalField(decimal_places=3, max_digits=65)
    voltage_generated_by_user = models.DecimalField(
        decimal_places=3, max_digits=65)
    activity = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
