from django.db import models
from django.utils import timezone




class BreakdownCategory(models.Model):
    breakdownCategoryId = models.AutoField(primary_key=True)
    breakdownCategoryName = models.CharField(max_length=100)

# class Shift(models.Model):
#     shiftId = models.AutoField(primary_key=True)
#     shift_name = models.CharField(max_length=100)
#     shift_start_time = models.TimeField()
#     shift_end_time = models.TimeField()
#     lunch_start_time = models.TimeField(blank=True, null=True)
#     lunch_end_time = models.TimeField(blank=True, null=True)

class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=100)

class Location(models.Model):
    locationId = models.AutoField(primary_key=True)
    locationName = models.CharField(max_length=100)

class Shopfloor(models.Model):
    shopfloorId = models.AutoField(primary_key=True)
    shopfloorName = models.CharField(max_length=100)

class Assemblyline(models.Model):
    assemblylineId = models.AutoField(primary_key=True)
    assemblylineName = models.CharField(max_length=100)

class Machine(models.Model):
    machineId = models.AutoField(primary_key=True)
    machineName = models.CharField(max_length=100)

class Andon(models.Model):
    # company = models.CharField(max_length=10, default='SKF')
    # location = models.CharField(max_length=10, default='BLR')
    # shopfloor = models.CharField(max_length=30, default='BALL BEARING')
    assemblyline = models.CharField(max_length=30)
    machineId = models.CharField(max_length=50)
    ticket = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    # alert_shift = models.CharField(max_length=10)
    andon_alerts = models.DateTimeField(null=True, blank=True)
    andon_acknowledge = models.DateTimeField(null=True, blank=True)
    andon_resolved = models.DateTimeField(null=True, blank=True)
    total_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'andon'


class AndonData(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=10, default='SKF')
    location = models.CharField(max_length=10, default='BLR')
    shopfloor = models.CharField(max_length=30, default='GRINDING')
    assemblyline = models.CharField(max_length=30)
    machineId = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    alert_shift = models.CharField(max_length=10)
    andon_alerts = models.CharField(max_length=100,null=True, blank=True)
    andon_acknowledge = models.CharField(max_length=100,null=True, blank=True)
    andon_resolved = models.CharField(max_length=100,null=True, blank=True)
    response_time = models.CharField(max_length=100, blank=True, null=True)
    repair_time = models.CharField(max_length=100, blank=True, null=True)
    total_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'andon_data'

class BreakdownHMI(models.Model):
    id = models.AutoField(primary_key=True)
    machine_id = models.CharField(max_length=55)
    channel_id = models.CharField(max_length=55)
    timestamp = models.DateTimeField()
    breakdown_alert = models.CharField(max_length=255)
    alert_value = models.IntegerField()

    class Meta:
        db_table = 'breakdown_hmi'