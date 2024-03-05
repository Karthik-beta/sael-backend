import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from production.models import WeeklyTarget
from datetime import datetime

class Command(BaseCommand):
    help = 'Read data from Excel file and compare with SpellAssemblyLineData model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            # Read the Excel file using pandas
            df = pd.read_excel(file_path)
            print("df: ", df)

            # Get or create an instance of WeeklyTarget
            weekly_target_instance, created = WeeklyTarget.objects.get_or_create()

            # Update fields from the DataFrame
            weekly_target_instance.w1_target = str(df.iloc[0, 1])
            weekly_target_instance.w1_actual = str(df.iloc[0, 2])

            weekly_target_instance.w2_target = str(df.iloc[1, 1])
            weekly_target_instance.w2_actual = str(df.iloc[1, 2])

            weekly_target_instance.w3_target = str(df.iloc[2, 1])
            weekly_target_instance.w3_actual = str(df.iloc[2, 2])

            weekly_target_instance.w4_target = str(df.iloc[3, 1])
            weekly_target_instance.w4_actual = str(df.iloc[3, 2])

            weekly_target_instance.save()

        except FileNotFoundError as fe:
            self.stdout.write(self.style.ERROR(f'File not found: {str(fe)}'))
        except pd.errors.ParserError as pe:
            self.stdout.write(self.style.ERROR(f'Error reading Excel file: {str(pe)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
