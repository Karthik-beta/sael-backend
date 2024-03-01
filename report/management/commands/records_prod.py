from django.core.management.base import BaseCommand
from production.models import productionPlanning, lineMachineConfig, lineMachineSlotConfig
from report.models import productionReport

from production import models as production_models
from config import models as config_models

class Command(BaseCommand):
    help = 'Copy data from production_planning to production_report'

    def handle(self, *args, **options):
        # Get the first job_id from ProductionPlanning
        job_id = production_models.productionPlanning.objects.first().job_id

        planning_data = productionPlanning.objects.all()

        for plan in planning_data:
            # Check if the record already exists in productionReport
            if not productionReport.objects.filter(job_id=job_id).exists():

                line_machine_config = lineMachineConfig.objects.filter(job_id=plan.job_id).first()

                productionReport.objects.create(
                    job_id=plan.job_id,
                    customer=plan.customer,
                    po_no=plan.po_no,
                    batch_no=plan.batch_no,
                    assigned_date=plan.assigned_date,
                    expected_date=plan.expected_date,
                    company = None,
                    plant = line_machine_config.plant if line_machine_config else None,
                    shopfloor = line_machine_config.shopfloor if line_machine_config else None,
                    assembly_line = line_machine_config.assembly_line if line_machine_config else None,
                    machine_id = line_machine_config.machine_id if line_machine_config else None,
                    product_id = line_machine_config.product_id if line_machine_config else None,
                    date = None,
                    shift_a = None,
                    shift_b = None,
                    shift_c = None,
                    planned_hours = None,
                    planned_production = None,
                    remaining_hours = None,
                    balance_production = None,
                    manager = line_machine_config.manager if line_machine_config else None,
                )
            
            
        self.stdout.write(self.style.SUCCESS('Data copied successfully.'))