# Generated by Django 4.2.6 on 2023-11-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0027_machinewisedata_machine_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionplanning',
            name='product_target',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
