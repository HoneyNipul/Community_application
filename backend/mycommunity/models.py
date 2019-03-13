from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from datetime import datetime
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Address(models.Model):
    def __str__(self):
        return self.address_line1 + ' ' + self.address_line2

    class Meta:
        db_table="Address"

    address_line1 = models.CharField(max_length=200, default='', blank=False)
    address_line2 = models.CharField(max_length=200, default='')
    landmark = models.CharField(max_length=100, default='')
    area = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    phone_number1 = models.CharField(max_length=10)
    phone_number2 = models.CharField(max_length=10)


class Member(models.Model):

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' '+ self.last_name

    class Meta:
        db_table="Member"

    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=16, choices=(("Female", "Female"), ("Male", "Male"),("other", "other")), default="Female")
    email = models.EmailField()
    occupation = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=16, choices=(("Married", "Married"), ("Unmarried", "Unmarried"),("Divorced", "Divorced"),("Widow", "Widow"),("Widower", "Widower")), default="Unmarried")
    birth_date = models.DateTimeField(default=datetime.now)
    mobile_number1 = models.CharField(max_length=16)
    mobile_number2 = models.CharField(max_length=16)
    office_number = models.CharField(max_length=16)
    photo = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Relation(models.Model):
    def __str__(self):
        return self.relation

    class Meta:
        db_table="Relation"

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="member_user")
    related_person = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="related_person_user" )
    relation = models.CharField(max_length=100)

class eventRegistration(models.Model):

    def __str__(self):
        return self.event_name

    class Meta:
        db_table="eventRegistration"

    event_name = models.CharField(max_length=200)
    inviters_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    event_description = models.TextField(max_length=3000)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_type = models.CharField(max_length=2, choices=(("PR", "Private"), ("PU", "Public")), default="PR")
    # location = models.CharField(max_length=200)
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # is_open_event = models.CharField(max_length=216)
    # Send_last_notification_before = models.DateTimeField()
    # event_photo = models.CharField(max_length=255)

class eventInvitee(models.Model):
    class Meta:
        db_table="eventInvitee"

    event_id = models.ForeignKey(eventRegistration, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)

# class eventnotification(models.Model):
#
#     class Meta:
#         db_table="Event_notification"
#
#     event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
#     notification_type = models.CharField(max_length=1056)
#     notification_description = models.TextField()
#     notification_start = models.DateField()
#     notification_end = models.DateField()

# class group(models.Model):
#
#     class Meta:
#         db_table="Group"
#
#     group_name = models.CharField(max_length=200)
#     admin_id = models.ForeignKey(Member, on_delete=models.CASCADE)
#
# class group_member(models.Model):
#
#     class Meta:
#         db_table="Group_Member"
#
#     group_id = models.ForeignKey(group, on_delete=models.CASCADE)
#     mem_id = models.ForeignKey(Member, on_delete=models.CASCADE)
#
# class inviteList(models.Model):
#     class Meta:
#         db_table = "inviteList"
#
#     event = models.ForeignKey(Events, on_delete=models.CASCADE)
#     inviteesId = models.ForeignKey(Member, on_delete=models.CASCADE)
#
#


