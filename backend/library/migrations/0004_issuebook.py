# Generated by Django 3.0.2 on 2020-02-06 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200202_1709'),
        ('library', '0003_auto_20200206_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library.BookInstance')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
