from django.core.management.base import BaseCommand
from production.models import soloAssemblyLineData

class Command(BaseCommand):
    help = 'Create 4 rows of solo assembly line data'

    def handle(self, *args, **options):
        # Define data for the 4 rows
        data = [
            {'stage_no': 1, 'stage': 'First Spell', 'mc_idle_hours': 60, 'target': 60},
            {'stage_no': 2, 'stage': 'Second Spell', 'mc_idle_hours': 60, 'target': 60},
            {'stage_no': 3, 'stage': 'Third Spell', 'mc_idle_hours': 60, 'target': 60},
            {'stage_no': 4, 'stage': 'Fourth Spell', 'mc_idle_hours': 60, 'target': 60},
        ]

        # Create soloAssemblyLineData objects
        for row_data in data:
            solo_assembly_data = soloAssemblyLineData(**row_data)
            solo_assembly_data.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 4 rows of solo assembly line data'))
