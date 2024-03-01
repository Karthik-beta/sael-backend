from django.core.management.base import BaseCommand
from production.models import productionPlanning, lineMachineConfig, lineMachineSlotConfig
from report.models import productionReport

class Command(BaseCommand):
    help = 'Copy data from production_planning and line_machine_config to production_report'

    def handle(self, *args, **options):
        # Query production_planning and line_machine_config
        planning_data = productionPlanning.objects.all()
        config_data = lineMachineSlotConfig.objects.all()

        # Iterate through the data and copy to production_report
        for plan in planning_data:
            try:
                config = config_data.get(job_id=plan.job_id)
            except lineMachineSlotConfig.DoesNotExist:
                config = None

            # Create a new production_report record if both planning and config data exist
            if config:
                productionReport.objects.create(
                    job_id=plan.job_id,
                    customer=plan.customer,
                    po_no=plan.po_no,
                    batch_no=plan.batch_no,
                    assigned_date=plan.assigned_date,
                    expected_date=plan.expected_date,
                    company=config.company,
                    plant=config.plant,
                    shopfloor=config.shopfloor,
                    assembly_line=config.assembly_line,
                    machine_id=config.machine_id,
                    product_id=config.product_id,
                    # date=plan.date,
                    shift_a=config.shift_a,
                    shift_b=config.shift_b,
                    shift_c=config.shift_c,
                    planned_hours=config.planned_hours,
                    planned_production=config.planned_production,
                    remaining_hours=config.remaining_hours,
                    balance_production=config.balance_production,
                    manager=config.manager,
                )

        self.stdout.write(self.style.SUCCESS('Data copied successfully.'))
