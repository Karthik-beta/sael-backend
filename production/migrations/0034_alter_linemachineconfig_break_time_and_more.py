# Generated by Django 4.2.6 on 2023-12-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0033_alter_linemachineconfig_assembly_line_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemachineconfig',
            name='break_time',
            field=models.CharField(blank=True, default='02:00:00', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='linemachineconfig',
            name='product_target',
            field=models.CharField(default='00:00:12', max_length=255),
        ),
        migrations.AlterField(
            model_name='machinewisedata',
            name='assembly_line',
            field=models.CharField(default='ASSEMBLYLINE-1', max_length=255),
        ),
        migrations.AlterField(
            model_name='machinewisedata',
            name='plant',
            field=models.CharField(default='CHENNAI', max_length=255),
        ),
        migrations.AlterField(
            model_name='machinewisedata',
            name='shopfloor',
            field=models.CharField(default='SHOPFLOOR-1', max_length=255),
        ),
    ]
