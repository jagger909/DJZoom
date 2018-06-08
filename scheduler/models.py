from django.db import models

from generic.choice_enum import ChoiceEnum
from enum import Enum
# Create your models here.


# class SchedulerManager(models.Manager):
# def create_scheduler(self):
# pass
#        scheduler = self.create(title=title)
# do something with the book
#       return book

TIME_CHOICES = (
    ('t1', '8:00-10:00'),
    ('t2', '10:00-12:00'),
    ('t3', '12:00-14:00'),
    ('t4', '14:00-16:00'),
    ('t5', '16:00-18:00'),
    ('t6', '18:00-20:00'),
    ('t7', '20:00-22:00'),
)


class TimeChoice(Enum):
    t1 = "8:00-10:00"
    t2 = "10:00-12:00"
    t3 = "12:00-14:00"
    t4 = "14:00-16:00"
    t5 = "16:00-18:00"
    t6 = "18:00-20:00"
    t7 = "20:00-22:00"

class Scheduler(models.Model):
    username = models.CharField(max_length=20)
    adres = models.CharField(max_length=200)
    telephone = models.CharField(max_length=12)
    comment = models.CharField(max_length=200)
    repair_date = models.DateField()
    repair_time = models.CharField(max_length=11, choices=[(tag.name, tag.value) for tag in TimeChoice])
    pub_date = models.DateTimeField(auto_now_add=True)

    # object = SchedulerManager()
    def __str__(self):
        return self.adres
