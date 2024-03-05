import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from production.models import MonthlyTarget
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

            monthly_target_instance, created = MonthlyTarget.objects.get_or_create()

            # monthly_target_instance.w1_shift = int(df.iloc[3, 1])
            # print("w1: ", monthly_target_instance.w1_shift)

            # monthly_target_instance.w2_shift = int(df.iloc[4, 1])

            # monthly_target_instance.w3_shift = int(df.iloc[5, 1])

            # monthly_target_instance.w4_shift = int(df.iloc[6, 1])

            # monthly_target_instance.shift_total = int(df.iloc[7, 1])

            # monthly_target_instance.w1_target = int(df.iloc[3, 2])

            # monthly_target_instance.w2_target = int(df.iloc[4, 2])

            # monthly_target_instance.w3_target = int(df.iloc[5, 2])

            # monthly_target_instance.w4_target = int(df.iloc[6, 2])

            # monthly_target_instance.target_total = int(df.iloc[7, 2])

            # monthly_target_instance.w1_production = str(df.iloc[3, 3])

            # monthly_target_instance.w2_production = str(df.iloc[4, 3])

            # monthly_target_instance.w3_production = str(df.iloc[5, 3])

            # monthly_target_instance.w4_production = str(df.iloc[6, 3])

            # monthly_target_instance.production_total = str(df.iloc[7, 3])

            # monthly_target_instance.today_rate = str(df.iloc[3, 4])

            # monthly_target_instance.days_completed = str(df.iloc[8, 1])

            # monthly_target_instance.holidays = str(df.iloc[8, 3])

            monthly_target_instance.save()

        except FileNotFoundError as fe:
            self.stdout.write(self.style.ERROR(f'File not found: {str(fe)}'))
        except pd.errors.ParserError as pe:
            self.stdout.write(self.style.ERROR(f'Error reading Excel file: {str(pe)}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unexpected error: {str(e)}'))
