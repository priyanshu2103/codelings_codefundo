from django.db import models

# Create your models here.


class donate_goods(models.Model):
    Name = models.CharField(max_length=100, blank=True)
    Phone_Number = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)
    Vehicles_Numbers = models.CharField(max_length=1000)
    Water = models.IntegerField()
    Packets_of_FoodItems = models.IntegerField()
    Medicines = models.CharField(max_length=10000)
    Date = models.DateField()

    def __str__(self):
        return 'Name: %s   Phone Number:%s  ' % (self.Name, self.Phone_Number)




