# Import necessary modules
import pandas as pd
from django.core.management.base import BaseCommand
from production.models import ExcelImport

class Command(BaseCommand):
    help = 'Import data from Excel file and save it to the ExcelImport model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            # Read the Excel file using pandas
            df = pd.read_excel(file_path)

            # Iterate through rows and save data to ExcelImport model with duplicate check
            for index, row in df.iterrows():
                # Check if the same data already exists
                if not ExcelImport.objects.filter(spells=row['Spells'], date=row['Date']).exists():
                    ExcelImport.objects.create(
                        spells=row['Spells'],
                        date=row['Date'],
                        shift=row['Shift'],
                        production=row['Production']
                    )

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
