from django.core.management import call_command
from django.test import TestCase
from datetime import date
from production.models import machineWiseData
from django.db import transaction

class TestMachineWiseDataCommand(TestCase):
    @transaction.atomic
    def test_machineWiseData_command(self):
        # Ensure no records exist with the same date and time
        self.assertFalse(machineWiseData.objects.filter(date=date.today()).exists())

        # Run the management command
        call_command('machinewise')

        # Print the content of the database for debugging
        print("Database content:")
        for item in machineWiseData.objects.all():
            print(f"ID: {item.id}, Date: {item.date}, Time: {item.time}")

        # Check if a new row was created with the expected time range
        self.assertTrue(machineWiseData.objects.filter(date=date.today(), time='13 - 14').exists())

        # Run the management command again to test the case when the row already exists
        call_command('machinewise')

        # Ensure that the command handles the case when the row already exists
        self.assertEqual(machineWiseData.objects.filter(date=date.today(), time='13 - 14').count(), 1)

        # Clean up by deleting the test row (if it was created)
        machineWiseData.objects.filter(date=date.today(), time='13 - 14').delete()
