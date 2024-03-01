from django.core.management.base import BaseCommand
from breakdown.models import AndonData, BreakdownHMI
from datetime import datetime, timedelta
from dateutil import parser

class Command(BaseCommand):
    help = 'Copy data from BreakdownHMI to AndonData'

    def handle(self, *args, **options):
        # Calculate the timestamp of 30 days ago
        thirty_days_ago = datetime.now() - timedelta(days=30)

        # Find all alerts that have been raised in the last 30 days
        raised_alerts = BreakdownHMI.objects.filter(alert_value=1, timestamp__gte=thirty_days_ago)

        for alert in raised_alerts:
            # Check if this alert has already been added to AndonData
            existing_alerts = AndonData.objects.filter(machineId=alert.machine_id, assemblyline=alert.channel_id, category=alert.breakdown_alert, andon_alerts=str(alert.timestamp)[:19])
            if existing_alerts.exists():
                # Check if there is an acknowledged alert for this AndonData object
                if existing_alerts.first().andon_acknowledge:
                    continue

                # Update the existing AndonData object with the alert data
                existing_alert = existing_alerts.first()
                existing_alert.andon_alerts = str(alert.timestamp)[:19]
                existing_alert.save()

                # Find the corresponding acknowledged alert
                acknowledged_alerts = BreakdownHMI.objects.filter(machine_id=alert.machine_id, channel_id=alert.channel_id, breakdown_alert=alert.breakdown_alert, alert_value=2, timestamp__gt=alert.timestamp)
                if acknowledged_alerts.exists():
                    acknowledged_alert = acknowledged_alerts.first()
                    existing_alert.andon_acknowledge = str(acknowledged_alert.timestamp.replace(tzinfo=None))[:19]
                    # Calculate the response time
                    response_time = datetime.strptime(existing_alert.andon_acknowledge, '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(existing_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                    existing_alert.response_time = str(response_time)

                # Find the corresponding resolved alert
                if existing_alert.andon_acknowledge:
                    resolved_alerts = BreakdownHMI.objects.filter(machine_id=alert.machine_id, channel_id=alert.channel_id, breakdown_alert=alert.breakdown_alert, alert_value=0, timestamp__gt=existing_alert.andon_acknowledge)
                    if resolved_alerts.exists():
                        resolved_alert = resolved_alerts.first()
                        existing_alert.andon_resolved = str(resolved_alert.timestamp.replace(tzinfo=None))[:19]
                        # Calculate the repair time
                        repair_time = datetime.strptime(str(resolved_alert.timestamp)[:19], '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(existing_alert.andon_acknowledge)[:19], '%Y-%m-%d %H:%M:%S')
                        existing_alert.repair_time = str(repair_time)

                # Calculate the alert shift
                andon_alert_time = datetime.strptime(str(existing_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                if 7 <= andon_alert_time.hour < 15:
                    existing_alert.alert_shift = "FS"
                elif 15 <= andon_alert_time.hour < 23:
                    existing_alert.alert_shift = "SS"
                elif 23 <= andon_alert_time.hour < 7:
                    existing_alert.alert_shift = "NS"

                # Calculate the total time
                if existing_alert.andon_alerts and existing_alert.andon_resolved:
                    total_time = datetime.strptime(str(existing_alert.andon_resolved)[:19], '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(existing_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                    existing_alert.total_time = str(total_time)

                existing_alert.save()

            else:
                # Create a new AndonData object with the alert data
                new_alert = AndonData(machineId=alert.machine_id, assemblyline=alert.channel_id, category=alert.breakdown_alert, andon_alerts=str(alert.timestamp)[:19])
                new_alert.save()

                # Find the corresponding acknowledged alert
                acknowledged_alerts = BreakdownHMI.objects.filter(machine_id=alert.machine_id, channel_id=alert.channel_id, breakdown_alert=alert.breakdown_alert, alert_value=2, timestamp__gt=alert.timestamp)
                if acknowledged_alerts.exists():
                    acknowledged_alert = acknowledged_alerts.first()
                    new_alert.andon_acknowledge = str(acknowledged_alert.timestamp.replace(tzinfo=None))[:19]
                    # Calculate the response time
                    response_time = datetime.strptime(new_alert.andon_acknowledge, '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(new_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                    new_alert.response_time = str(response_time)

                # Find the corresponding resolved alert
                if new_alert.andon_acknowledge:
                    resolved_alerts = BreakdownHMI.objects.filter(machine_id=alert.machine_id, channel_id=alert.channel_id, breakdown_alert=alert.breakdown_alert, alert_value=0, timestamp__gt=new_alert.andon_acknowledge)
                    if resolved_alerts.exists():
                        resolved_alert = resolved_alerts.first()
                        new_alert.andon_resolved = str(resolved_alert.timestamp.replace(tzinfo=None))[:19]
                        # Calculate the repair time
                        repair_time = datetime.strptime(str(resolved_alert.timestamp)[:19], '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(new_alert.andon_acknowledge)[:19], '%Y-%m-%d %H:%M:%S')
                        new_alert.repair_time = str(repair_time)

                # Calculate the alert shift
                andon_alert_time = datetime.strptime(str(new_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                if 7 <= andon_alert_time.hour < 15:
                    new_alert.alert_shift = "FS"
                elif 15 <= andon_alert_time.hour < 23:
                    new_alert.alert_shift = "SS"
                elif 23 <= andon_alert_time.hour < 7:
                    new_alert.alert_shift = "NS"

                # Calculate the total time
                if new_alert.andon_alerts and new_alert.andon_resolved:
                    total_time = datetime.strptime(str(new_alert.andon_resolved)[:19], '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(new_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                    new_alert.total_time = str(total_time)

                new_alert.save()

        # Update the andon_resolved field with the timestamp of the corresponding alert_value=0 record
        resolved_alerts = BreakdownHMI.objects.filter(alert_value=0)
        for resolved_alert in resolved_alerts:
            existing_alerts = AndonData.objects.filter(machineId=resolved_alert.machine_id, assemblyline=resolved_alert.channel_id, category=resolved_alert.breakdown_alert, andon_resolved=None, andon_acknowledge__lt=resolved_alert.timestamp)
            if existing_alerts.exists():
                existing_alert = existing_alerts.first()
                existing_alert.andon_resolved = str(resolved_alert.timestamp)[:19]
                # Calculate the repair time
                repair_time = datetime.strptime(str(resolved_alert.timestamp)[:19], '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(existing_alert.andon_acknowledge)[:19], '%Y-%m-%d %H:%M:%S')
                existing_alert.repair_time = str(repair_time)
                # Calculate the total time
                total_time = datetime.strptime(str(resolved_alert.timestamp)[:19], '%Y-%m-%d %H:%M:%S') - datetime.strptime(str(existing_alert.andon_alerts)[:19], '%Y-%m-%d %H:%M:%S')
                existing_alert.total_time = str(total_time)
                existing_alert.save()
        

        # Print a success message to the console
        self.stdout.write(self.style.SUCCESS('Successfully processed alert values and updated or created andon_data table entries for the last 30 days and newer ones.'))