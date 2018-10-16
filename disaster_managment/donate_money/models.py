from django.db import models

# Create your models here.


class donate_money(models.Model):
    Name = models.CharField(max_length=100, default='', blank=True)
    Phone_Number = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)
    Amount = models.IntegerField()

    def __str__(self):
        return '%s donated %s amount of money' % (self.Name, self.Amount)
