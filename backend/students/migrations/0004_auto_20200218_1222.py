# Generated by Django 3.0.3 on 2020-02-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200202_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], max_length=20),
        ),
    ]