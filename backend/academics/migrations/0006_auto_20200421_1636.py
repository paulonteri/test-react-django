# Generated by Django 3.0.3 on 2020-04-21 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_auto_20200421_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['-name'], 'verbose_name_plural': 'Subjects'},
        ),
        migrations.AlterModelOptions(
            name='subjectteacherclass',
            options={'ordering': ['-Class', '-teacher']},
        ),
    ]
