# Generated by Django 3.0.2 on 2020-02-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200206_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={},
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='available',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='date_due_back',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='student',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
