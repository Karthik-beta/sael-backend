import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from production.models import spellAssemblyLineData
from datetime import datetime

class Command(BaseCommand):
    help = 'Read date from Excel file and compare with SpellAssemblyLineData model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            # Read the Excel file using pandas
            df = pd.read_excel(file_path)
            print("df: ", df)

            # Extract date from 'B2' cell in Excel
            excel_date_str = str(df.iloc[0, 1])  # Assuming the date is in the first row, second column
            print("excel_date_str: ", excel_date_str)

            # Extract date from 'B2' cell in Excel
            excel_date_str = str(df.iloc[0, 1])  # Assuming the date is in the first row, second column
            print("excel_date_str: ", excel_date_str)

            excel_date = None  # or any default value
            if excel_date_str:
                try:
                    excel_date = datetime.strptime(excel_date_str, '%Y-%m-%d %H:%M:%S').date()
                except ValueError:
                    raise CommandError('Error: Invalid date format in Excel file')
            else:
                raise CommandError('Error: Missing date in Excel file')
            
            print("excel_date: ", excel_date)

            # Retrieve the latest SpellAssemblyLineData with the matching date
            latest_spell_data = spellAssemblyLineData.objects.filter(date=excel_date).last()
            print("latest_spell_data: ", latest_spell_data.date)

            # Check if data with the specified date exists
            if latest_spell_data:
                self.stdout.write(self.style.SUCCESS('Success: Data found for the specified date'))
            else:
                self.stdout.write(self.style.ERROR('Error: No data found for the specified date'))

            # Compare the two dates
            if latest_spell_data and excel_date == latest_spell_data.date:
                self.stdout.write(self.style.SUCCESS('Success: Dates match'))
            else:
                self.stdout.write(self.style.ERROR('Error: Dates do not match'))

            # Check if data with the specified date exists
            if latest_spell_data:
                self.stdout.write(self.style.SUCCESS('Success: Data found for the specified date'))
            else:
                self.stdout.write(self.style.ERROR('Error: No data found for the specified date'))  


        except FileNotFoundError as fe:
            self.stdout.write(self.style.ERROR(f'File not found: {str(fe)}'))
        except pd.errors.ParserError as pe:
            self.stdout.write(self.style.ERROR(f'Error reading Excel file: {str(pe)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
