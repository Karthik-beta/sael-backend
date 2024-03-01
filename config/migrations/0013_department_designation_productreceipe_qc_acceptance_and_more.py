# Generated by Django 4.2.6 on 2023-12-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0012_alter_productreceipe_skill_matrix'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('designation_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='productreceipe',
            name='QC_acceptance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productreceipe',
            name='tolerance',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
