# train_schedule/models.py

from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    delay_minutes = models.IntegerField()
    sleeper_price = models.DecimalField(max_digits=10, decimal_places=2)
    ac_price = models.DecimalField(max_digits=10, decimal_places=2)
    sleeper_seats_available = models.PositiveIntegerField()
    ac_seats_available = models.PositiveIntegerField()

    class Meta:
        app_label = 'train_schedule'




class CompanyRegistration(models.Model):
    company_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=20)
    owner_email = models.EmailField()
    access_code = models.CharField(max_length=20)
    client_id = models.CharField(max_length=36, blank=True, null=True)
    client_secret = models.CharField(max_length=16, blank=True, null=True)
