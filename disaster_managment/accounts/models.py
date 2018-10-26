from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

#
# class CustomUser(AbstractUser):
#     age = models.PositiveIntegerField("age", null=True)


class Volunteer(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100,blank=True)
    Age = models.IntegerField(max_length=3)
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    State = models.CharField(max_length=20)
    City = models.CharField(max_length=40)
    Locality = models.CharField(max_length=100)
    Pin = models.IntegerField(max_length=6)
    PhoneNumber = models.IntegerField(max_length=10)

    def __str__(self):
        return 'Username: %s   Phone Number:%s  ' % (self.username, self.PhoneNumber)


# @receiver(post_save, sender=User)
# def create_volunteer_profile(sender, instance, created, **kwargs):
#     if created:
#         Volunteer.objects.create(user=instance)
#
#
# @receiver(post_save, sender=Volunteer)
# def save_volunteer_profile(sender,instance,**kwargs):
#     instance.profile.save()


