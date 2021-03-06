# Generated by Django 3.0.3 on 2020-04-21 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_auto_20200411_0651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classes',
            options={'ordering': ['-class_numeral', '-stream'], 'verbose_name_plural': 'Class + Streams (Normal Classes)'},
        ),
        migrations.AlterModelOptions(
            name='classnumeral',
            options={'ordering': ['-name'], 'verbose_name_plural': 'Class Numerals'},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ['-exam_start_date', '-name']},
        ),
        migrations.AlterModelOptions(
            name='stream',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='subjectteacher',
            options={'ordering': ['-subject', '-teacher']},
        ),
        migrations.RemoveField(
            model_name='exam',
            name='year',
        ),
    ]
