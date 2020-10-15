# Generated by Django 3.0.2 on 2020-02-02 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('other_name', models.CharField(blank=True, max_length=20, null=True)),
                ('national_id', models.IntegerField(help_text='Enter National ID. This is not editable!', primary_key=True, serialize=False)),
                ('kra_pin', models.CharField(max_length=11, unique=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('home_town', models.CharField(blank=True, max_length=20, null=True)),
                ('home_county', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact_name', models.CharField(max_length=40, null=True)),
                ('emergency_contact_relationship', models.CharField(help_text='Eg: Close Uncle', max_length=10, null=True)),
                ('emergency_phone', models.IntegerField(help_text='Enter Emergency phone number', null=True)),
                ('health_condition', models.TextField(blank=True, default='Good', help_text='Enter health status or complications', max_length=500, null=True)),
                ('is_employed', models.BooleanField(default=True)),
                ('is_teaching_staff', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'staff',
                'ordering': ['surname', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='StaffRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(help_text='Staff roles. Eg;Teacher,Cook,Secretary,e.t.c', max_length=20, unique=True)),
                ('role_function', models.TextField(max_length=500)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsc_number', models.IntegerField(unique=True)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now=True)),
                ('staff_info', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='staff.Staff')),
            ],
            options={
                'verbose_name_plural': 'Teaching Staff',
                'ordering': ['tsc_number'],
            },
        ),
        migrations.AddField(
            model_name='staff',
            name='role',
            field=models.ForeignKey(help_text='Staff roles. Eg;Teacher,Cook,Secretary,e.t.c', null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.StaffRole'),
        ),
    ]