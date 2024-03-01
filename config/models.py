from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    product_Name = models.CharField(max_length=100)
    drawing_no = models.CharField(max_length=100)
    stages = models.IntegerField(null=True)

    class Meta:
        db_table = 'products'


class company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'company'


class plant(models.Model):
    id = models.AutoField(primary_key=True)
    plant_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'plant'


class shopfloor(models.Model):
    id = models.AutoField(primary_key=True)
    shopfloor_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'shopfloor'


class assemblyline(models.Model):
    id = models.AutoField(primary_key=True)
    assemblyline_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'assemblyline'


class machine(models.Model):
    id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'machine'


class batch(models.Model):
    id = models.AutoField(primary_key=True)
    batch_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'batch'


class poNo(models.Model):
    id = models.AutoField(primary_key=True)
    po_no = models.CharField(max_length=100)

    class Meta:
        db_table = 'po_no'


class department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'department'


class designation(models.Model):
    id = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=255)


# class productReceipe(models.Model):
#     id = models.AutoField(primary_key=True)
#     product_Name = models.CharField(max_length=100)
#     stages = models.IntegerField()
#     target_per_unit = models.DurationField()
#     units_per_minute = models.FloatField(blank=True, null=True)
#     units_per_hour = models.FloatField(blank=True, null=True)
#     skill_matrix = models.CharField(max_length=255)
#     QC_acceptance = models.CharField(max_length=255, blank = True, null =True)
#     tolerance = models.CharField(max_length=255, blank = True, null =True)

#     def save(self, *args, **kwargs):
#         # Calculate units_per_minute and units_per_hour based on target_per_unit
#         if self.target_per_unit:
#             minutes = self.target_per_unit.total_seconds() 
#             units_per_minute = 60 / minutes if minutes > 0 else 0
#             self.units_per_minute = round(60 / minutes, 2) if minutes > 0 else 0
#             self.units_per_hour = round(units_per_minute * 60, 2)
#         else:
#             self.units_per_minute = 0
#             self.units_per_hour = 0

#         super(productReceipe, self).save(*args, **kwargs)

#     class Meta:
#         db_table = 'product_receipe'



class ProductRecipe2(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    stages = models.JSONField()
    
    class Meta:
        db_table = 'product_recipe2'


class attendanceRules(models.Model):
    id = models.AutoField(primary_key=True)
    shift_name = models.CharField(max_length=100)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    late_grace_time = models.TimeField()
    early_grace_time = models.TimeField()

    class Meta:
        db_table = 'attendance_rules'


class InspectionParameters(models.Model):
    id = models.AutoField(primary_key=True)
    parameter_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'inspection_parameters'
        

class QCDefectType(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    parameter_id = models.ForeignKey(InspectionParameters, on_delete=models.CASCADE)
    defect_name = models.CharField(max_length=255)
    defect_code = models.CharField(max_length=255)

    class Meta:
        db_table = 'qc_defect_type'





class ShiftTiming(models.Model):
    id = models.AutoField(primary_key=True)
    shift_name = models.CharField(max_length=100)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    lunch_break_start = models.TimeField()
    lunch_break_end = models.TimeField()
    tea_break_1_start = models.TimeField()
    tea_break_1_end = models.TimeField()
    tea_break_2_start = models.TimeField()
    tea_break_2_end = models.TimeField()
    tea_break_3_start = models.TimeField()
    tea_break_3_end = models.TimeField()
    cleaning_start_time = models.TimeField()
    cleaning_end_time = models.TimeField()
    spell_downtime = models.DurationField()
    total_working_hours = models.DurationField()

    class Meta:
        db_table = 'shift_timing'