# Generated by Django 3.0.3 on 2020-03-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_issuebook_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
