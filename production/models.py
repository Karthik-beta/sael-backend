from django.db import models
from datetime import datetime, date

from datetime import datetime, timedelta
from config.models import ProductRecipe2

from config import models as config_models


# def build_id(self, id):
#         join_dates = str(datetime.now().strftime('%Y%m%d'))
#         return (('JW-' + join_dates) + '-' + str(id))

# def increment_helpdesk_number():
#     last_helpdesk = productionPlanning.objects.all().order_by('id').last()

#     if not last_helpdesk:
#         return 'JW-' + str(datetime.now().strftime('%Y%m%d-')) + '0000'

#     help_id = last_helpdesk.job_id
#     help_int = ''.join(c for c in help_id[13:17] if c.isdigit())
#     new_help_int = int(help_int) + 1
#     new_help_id = 'JW-' + str(datetime.now().strftime('%Y%m%d-')) + str(new_help_int).zfill(4)

#     return new_help_id


class productionPlanning(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.CharField(max_length=100, default='', unique=True)
    employee_id = models.CharField(max_length=100, default='1')
    product_id = models.CharField(max_length=100)
    drawing_no = models.CharField(max_length=100, blank=True, null=True)
    customer = models.CharField(max_length=100)
    po_no = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=100)
    quantity = models.IntegerField()
    assigned_date = models.DateField(blank=True, null=True)
    expected_date = models.DateField(blank=True, null=True)
    planned_date = models.DateField(blank=True, null=True)
    processing_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    required_time = models.CharField(max_length=255, blank=True, null=True)
    product_target = models.DurationField(blank=True, null=True)

    # def jobwork_generator(self, id):
    #     join_dates = str(datetime.now().strftime('%Y%m%d'))
    #     return (('JW-' + join_dates) + '-' + str(id))
    def jobwork_generator(self):
        join_dates = str(datetime.now().strftime('%Y%m%d'))
        return f'JW-{join_dates}-{self.id}'
    
    def get_drawing_no(self):
        try:
            product = config_models.Products.objects.get(product_Name=self.product_id)
            drawing_no = product.drawing_no
        except config_models.Products.DoesNotExist:
            # Handle the case where the product doesn't exist in Products
            drawing_no = None

        return drawing_no
    

    '''Old but works'''
    # def calculate_required_time(self):
    #      # Assuming product_id is used to link to the productReceipe model
    #     try:
    #         product_recipe = config_models.productReceipe.objects.get(product_Name=self.product_id)
    #         product_target = product_recipe.target_per_unit
    #     except config_models.productReceipe.DoesNotExist:
    #         product_target = None

    #     if product_target:
    #         product_target_seconds = product_target.total_seconds()
    #     else:
    #         # Set a default value or raise an exception as needed
    #         product_target_seconds = 0

    #     # Set the product_target field
    #     self.product_target = product_target

    #     # Assuming product target is 60 seconds
    #     # product_target_seconds = self.product_target.total_seconds() if self.product_target else 0
    #     total_seconds = product_target_seconds * self.quantity

    #     # Convert total_seconds to HH:MM format
    #     required_time_hours, remainder = divmod(total_seconds, 3600)
    #     required_time_minutes, _ = divmod(remainder, 60)

    #     # Format the result as HH:MM
    #     # required_time = "{:02}:{:02}".format(required_time_hours, required_time_minutes)

    #      # Format the result as HH:MM
    #     required_time = "{:02}:{:02}".format(int(required_time_hours), int(required_time_minutes))

    #     return required_time
        
    
    def calculate_required_time(self):
        try:
            product_recipe = ProductRecipe2.objects.get(product_name=self.product_id)
            stages = product_recipe.stages
            total_target_seconds = 0

            for stage in stages:
                target_per_unit_str = stage.get("target_per_unit", "00:00:00")
                target_per_unit = datetime.strptime(target_per_unit_str, "%H:%M:%S").time()
                target_seconds = target_per_unit.hour * 3600 + target_per_unit.minute * 60 + target_per_unit.second
                total_target_seconds += target_seconds

            # Assuming total_target_seconds is the sum of target_per_unit for all stages
            total_seconds = total_target_seconds * self.quantity

            required_time_hours, remainder = divmod(total_seconds, 3600)
            required_time_minutes, _ = divmod(remainder, 60)

            required_time = "{:02}:{:02}".format(int(required_time_hours), int(required_time_minutes))

            self.product_target = timedelta(seconds=total_target_seconds)

            return required_time
        except ProductRecipe2.DoesNotExist:
            # Handle the case where the product recipe doesn't exist
            return "00:00"

    
    # def save(self, *args, **kwargs):
    #     if not self.job_id:
    #         self.job_id = self.jobwork_generator(self.id)

    #     # Set assigned_date to the current date if not already set
    #     if not self.assigned_date:
    #         self.assigned_date = datetime.now().date()

    #     # Calculate and set required_time
    #     self.required_time = self.calculate_required_time()

    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.job_id:
            # Set assigned_date to the current date if not already set
            if not self.assigned_date:
                self.assigned_date = datetime.now().date()

            # Calculate and set required_time
            self.required_time = self.calculate_required_time()

            # Save the instance
            super().save(*args, **kwargs)

            # Generate job_id using jobwork_generator after the instance is saved
            self.job_id = self.jobwork_generator()
            self.drawing_no = self.get_drawing_no()
            
            # Update the instance with the generated job_id
            super().save(update_fields=['job_id', 'drawing_no'])

    class Meta:
        db_table = 'production_planning'





class lineMachineConfig(models.Model):
    id = models.AutoField(primary_key=True)
    # production_planning = models.ForeignKey(productionPlanning, on_delete=models.CASCADE)
    job_id = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    plant = models.CharField(max_length=255)
    shopfloor = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    product_target = models.CharField(max_length=255)
    assembly_line = models.CharField(max_length=255)
    machine_id = models.CharField(max_length=255)
    total_order = models.IntegerField(blank=True, null=True)
    required_time = models.CharField(max_length=255, blank=True, null=True)
    break_time = models.CharField(max_length=255, blank=True, null=True, default='02:00:00')
    assigned_start_production = models.CharField(max_length=255, blank=True, null=True)
    assigned_end_production = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255)
    stage_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'line_machine_config'



class lineMachineSlotConfig(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    plant = models.CharField(max_length=255)
    shopfloor = models.CharField(max_length=255)
    assembly_line = models.CharField(max_length=255)
    machine_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    date = models.DateField()
    shift_a = models.CharField(max_length=255, blank=True, null=True)
    shift_b = models.CharField(max_length=255, blank=True, null=True)
    shift_c = models.CharField(max_length=255,blank=True, null=True)
    planned_hours = models.IntegerField()
    planned_production = models.IntegerField(blank=True, null=True)
    remaining_hours = models.IntegerField()
    balance_production = models.IntegerField()
    manager = models.CharField(max_length=255, default='XYZ')

    class Meta:
        db_table = 'line_machine_slot_config'




class machineWiseData(models.Model):
    id = models.AutoField(primary_key=True)
    plant = models.CharField(max_length=255, default='Ferozepur')
    shopfloor = models.CharField(max_length=255, default='Module Line - 1')
    assembly_line = models.CharField(max_length=255, default='NA')
    machine_id = models.CharField(max_length=255)
    product_target = models.IntegerField(default=60)
    time = models.CharField(max_length=255)
    date = models.DateField()
    # date = models.DateField(default=date.today)    #production sauld
    on_time = models.IntegerField(blank=True, null=True)
    idle_time = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True, default=300)
    performance = models.FloatField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'machine_wise_data'
        unique_together = ('machine_id', 'date', 'time')

    # def save(self, *args, **kwargs):
        # current_time = datetime.now()
        # current_hour = current_time.hour
        # time_range = f'{current_hour:02d} - {current_hour+1:02d}'
        
        # # Check if a record with the same date and time already exists
        # if not machineWiseData.objects.filter(date=self.date, time=time_range).exists():
        #     self.time = time_range
        #     super(machineWiseData, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Calculate idle_time as 60 - on_time
        self.idle_time = 60 - self.on_time if self.on_time is not None else 60

        # Calculate performance as (actual / target) * 100
        if self.target is not None and self.actual is not None:
            self.performance = round((self.actual / self.target) * 100, 2)
        else:
            self.performance = 0

        super(machineWiseData, self).save(*args, **kwargs)



class assemblyLineWiseData(models.Model):
    id = models.AutoField(primary_key=True)
    plant = models.CharField(max_length=255)
    shopfloor = models.CharField(max_length=255)
    assemblyline = models.CharField(max_length=255)
    machine_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    date_production = models.CharField(max_length=255)
    # stages = models.JSONField()
    shift_name = models.CharField(max_length=255)


# class soloAssemblyLineData(models.Model):
#     id = models.AutoField(primary_key=True)
#     assembly_line_data = models.ForeignKey(assemblyLineWiseData, on_delete=models.CASCADE)
#     stage_no = models.IntegerField()
#     stage_name = models.CharField(max_length=255)
#     mc_on_hours = models.IntegerField()
#     mc_idle_hours = models.IntegerField()
#     actual = models.IntegerField()
#     target = models.IntegerField()
#     performance = models.FloatField()
#     current = models.FloatField()

#     class Meta:
#         db_table = 'solo_assembly_line_data'
    

class soloAssemblyLineData(models.Model):
    id = models.AutoField(primary_key=True)
    stage_no = models.IntegerField()
    stage = models.CharField(max_length=255)
    mc_on_hours = models.IntegerField(blank=True, null=True)
    mc_idle_hours = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)
    performance = models.FloatField(blank=True, null=True)
    gap = models.IntegerField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)  
    shift = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'solo_assembly_line_data'

    def save(self, *args, **kwargs):
        # Calculate idle_time as 60 - on_time
        # self.mc_idle_hours = 660 - self.mc_on_hours if self.mc_on_hours is not None else None

        if self.mc_idle_hours is not None and self.mc_on_hours is not None:
            self.mc_idle_hours = 600 - self.mc_on_hours
        else:
            self.mc_idle_hours = 600

        # Calculate performance as (actual / target) * 100
        if self.target is not None and self.actual is not None:
            self.performance = round((self.actual / self.target) * 100, 2)
        else:
            self.performance = 0
        
        if self.target is not None and self.actual is not None:
            self.gap = self.actual - self.target
        else:
            self.gap = 0

        super(soloAssemblyLineData, self).save(*args, **kwargs)


class ProductionAndon(models.Model):
    s_no = models.AutoField(primary_key=True)
    machine_id = models.CharField(max_length=255, blank=True, null=True)
    machine_datetime = models.DateTimeField(blank=True, null=True)
    machine_status = models.CharField(max_length=255, blank=True, null=True)
    production_count = models.CharField(max_length=255, blank=True, null=True)
    kwh_reading = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_andon'



class spellAssemblyLineData(models.Model):
    id = models.AutoField(primary_key=True)
    stage_no = models.IntegerField()
    stage = models.CharField(max_length=255)
    mc_on_hours = models.IntegerField(blank=True, null=True)
    mc_idle_hours = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)
    performance = models.FloatField(blank=True, null=True)
    gap = models.IntegerField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)  
    shift = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'spell_assembly_line_data'

    def save(self, *args, **kwargs):
        # Calculate idle_time as 60 - on_time
        # self.mc_idle_hours = 660 - self.mc_on_hours if self.mc_on_hours is not None else None

        if self.mc_idle_hours is not None and self.mc_on_hours is not None:
            self.mc_idle_hours = 600 - self.mc_on_hours
        else:
            self.mc_idle_hours = 600

        # Calculate performance as (actual / target) * 100
        if self.target is not None and self.actual is not None:
            self.performance = round((self.actual / self.target) * 100, 2)
        else:
            self.performance = 0
        
        if self.target is not None and self.actual is not None:
            self.gap = self.actual - self.target
        else:
            self.gap = 0

        super(spellAssemblyLineData, self).save(*args, **kwargs)


# class ExcelImport(models.Model):
#     field1 = models.CharField(max_length=255)
#     field2 = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'excel_import'


class ExcelImport(models.Model):
    spells = models.CharField(max_length=255)
    date = models.DateField()
    shift = models.CharField(max_length=55)
    production = models.PositiveIntegerField()
    target= models.PositiveIntegerField()
    gap = models.PositiveIntegerField()

    class Meta:
        db_table = 'excel_import'
        
