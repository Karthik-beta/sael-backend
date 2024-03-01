from django.core.management.base import BaseCommand
from datetime import date, datetime, timedelta
from production.models import machineWiseData
from config import models as config_models

class Command(BaseCommand):
    help = 'Creates machineWiseData objects for each machine and time range'

    def handle(self, *args, **options):
        current_date = date.today()
        
        # Create records for each hour from 08:00 to 20:00
        for current_hour in range(8, 21):
            start_time = datetime(current_date.year, current_date.month, current_date.day, current_hour, 0)
            end_time = start_time + timedelta(hours=1)
            time_range = f'{start_time.strftime("%H:%M")} - {end_time.strftime("%H:%M")}'
            
            # Check if a record with the same date and time already exists
            if machineWiseData.objects.filter(date=current_date, time=time_range).exists():
                self.stdout.write(self.style.SUCCESS(f'A row with time range {time_range} already exists for today.'))
            else:
                # Get a list of all machines from the 'machine' model
                machines = config_models.machine.objects.all()

                for machine_instance in machines:
                    # Create a new 'machineWiseData' instance for each machine and time range
                    machine_data = machineWiseData(
                        date=current_date,
                        time=time_range,
                        machine_id=machine_instance.machine_name  # Copy 'machine_name' to 'machine_id'
                    )
                    machine_data.save()
                    self.stdout.write(self.style.SUCCESS(f'Created a new row for machine: {machine_instance.machine_name}, time range: {time_range}'))
