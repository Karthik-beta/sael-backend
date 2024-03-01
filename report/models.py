from django.db import models






'''Management file for production report'''
class productionReport(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.CharField(max_length=100, unique=True)
    customer = models.CharField(max_length=100)
    po_no = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=100)
    assigned_date = models.DateField(blank=True, null=True)
    expected_date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    plant = models.CharField(max_length=255, blank=True, null=True)
    shopfloor = models.CharField(max_length=255, blank=True, null=True)
    assembly_line = models.CharField(max_length=255, blank=True, null=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    shift_a = models.CharField(max_length=255, blank=True, null=True)
    shift_b = models.CharField(max_length=255, blank=True, null=True)
    shift_c = models.CharField(max_length=255, blank=True, null=True)
    planned_hours = models.IntegerField(blank=True, null=True)
    planned_production = models.IntegerField(blank=True, null=True)
    remaining_hours = models.IntegerField(blank=True, null=True)
    balance_production = models.IntegerField(blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'production_report'