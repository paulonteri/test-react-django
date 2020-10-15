from django.db import models
from django.urls import reverse


# add user model
class StaffRole(models.Model):
    role = models.CharField(max_length=20, unique=True,
                            help_text="Staff roles. Eg;Teacher,Cook,Secretary,e.t.c")
    role_function = models.TextField(max_length=500)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role


class Staff(models.Model):
    role = models.ForeignKey(StaffRole, on_delete=models.SET_NULL, help_text="Staff roles. Eg;Teacher,Cook,"
                                                                             "Secretary,e.t.c", null=True)
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    other_name = models.CharField(blank=True, null=True, max_length=20)
    national_id = models.IntegerField(primary_key=True, help_text="Enter National ID. This is not "
                                                                  "editable!")
    kra_pin = models.CharField(max_length=11, unique=True)
    phone = models.IntegerField()
    email = models.EmailField()
    home_town = models.CharField(max_length=20, null=True, blank=True)
    home_county = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_name = models.CharField(null=True, max_length=40)
    emergency_contact_relationship = models.CharField(
        null=True, max_length=10, help_text="Eg: Close Uncle")
    emergency_phone = models.IntegerField(
        null=True, help_text="Enter Emergency phone number")
    health_condition = models.TextField(max_length=500, null=True, blank=True, default="Good", help_text="Enter "
                                                                                                         "health "
                                                                                                         "status or "
                                                                                                         "complications")
    is_employed = models.BooleanField(default=True)
    is_teaching_staff = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.role.role}: {self.surname} {self.first_name}'

    def get_absolute_url(self):
        reverse('staff_detail', args=[str(self.national_id)])

    class Meta:
        verbose_name_plural = "staff"
        ordering = ['surname', 'first_name']


class TeachingStaff(models.Model):
    # subjects
    staff_info = models.OneToOneField(Staff, on_delete=models.PROTECT)
    tsc_number = models.IntegerField(unique=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        reverse('teaching_staff_detail', args=[str(self.staff_info)])

    def __str__(self):
        return f'{self.staff_info.role}: {self.staff_info.surname} {self.staff_info.first_name}'

    class Meta:
        verbose_name_plural = "Teaching Staff"
        ordering = ["tsc_number"]
