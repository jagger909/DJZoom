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

# TIME_CHOICES = (
#     ('t1', '8:00-10:00'),
#     ('t2', '10:00-12:00'),
#     ('t3', '12:00-14:00'),
#     ('t4', '14:00-16:00'),
#     ('t5', '16:00-18:00'),
#     ('t6', '18:00-20:00'),
#     ('t7', '20:00-22:00'),
# )

class Scheduler(models.Model):

    class TimeChoice(ChoiceEnum):
        T1 = "08:00-11:00"
        T2 = "10:00-13:00"
        T3 = "12:00-15:00"
        T4 = "14:00-17:00"
        T5 = "16:00-19:00"
        T6 = "18:00-21:00"
        # T7 = "20:00-23:00"

    username = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    telephone = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True)
    repair_date = models.DateField()
    repair_time = models.CharField(max_length=2, choices=TimeChoice.choices(), default=TimeChoice.T1)
    pub_date = models.DateTimeField(auto_now_add=True)
    sched_un_id = models.CharField(db_index= True, unique=True, max_length=10)

    # object = SchedulerManager()
    def __str__(self):
        return self.address
