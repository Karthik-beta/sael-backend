from django.core.management.base import BaseCommand
from datetime import datetime, date
from production.models import machineWiseData

from config import models as config_models



'''Just create new single object for machineWiseData model'''
# class Command(BaseCommand):
#     help = 'Creates a new machineWiseData object'

#     def handle(self, *args, **options):
#         current_date = date.today()
#         current_time = datetime.now()
#         current_hour = current_time.hour
#         time_range = f'{current_hour:02d} - {current_hour+1:02d}'
        
#         # Check if a record with the same date and time already exists
#         if machineWiseData.objects.filter(date=current_date, time=time_range).exists():
#             self.stdout.write(self.style.SUCCESS(f'A row with time range {time_range} already exists for today.'))
#         else:
#             machine_data = machineWiseData(date=current_date, time=time_range)
#             machine_data.save()
#             self.stdout.write(self.style.SUCCESS(f'Created a new row with time range: {time_range}'))



'''create new single object for every machine model for every hour'''
class Command(BaseCommand):
    help = 'Creates a new machineWiseData object for each machine'

    def handle(self, *args, **options):
        current_date = date.today()
        current_time = datetime.now()
        current_hour = current_time.hour
        time_range = f'{current_hour:02d} - {current_hour+1:02d}'
        
        # Check if a record with the same date and time already exists
        if machineWiseData.objects.filter(date=current_date, time=time_range).exists():
            self.stdout.write(self.style.SUCCESS(f'A row with time range {time_range} already exists for today.'))
        else:
            # Get a list of all machines from the 'machine' model
            machines = config_models.machine.objects.all()

            for machine_instance in machines:
                # Create a new 'machineWiseData' instance for each machine
                machine_data = machineWiseData(
                    date=current_date,
                    time=time_range,
                    machine_id=machine_instance.machine_name  # Copy 'machine_name' to 'machine_id'
                )
                machine_data.save()
                self.stdout.write(self.style.SUCCESS(f'Created a new row for machine: {machine_instance.machine_name}, time range: {time_range}'))