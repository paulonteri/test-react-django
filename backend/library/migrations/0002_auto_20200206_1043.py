# Generated by Django 3.0.2 on 2020-02-06 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200202_1709'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Student'),
        ),
    ]