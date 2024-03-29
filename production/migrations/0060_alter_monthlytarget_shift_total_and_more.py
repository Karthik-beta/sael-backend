# Generated by Django 4.2.6 on 2024-03-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0059_monthlytarget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytarget',
            name='shift_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlytarget',
            name='today_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlytarget',
            name='w1_shift',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlytarget',
            name='w2_shift',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlytarget',
            name='w3_shift',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlytarget',
            name='w4_shift',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
