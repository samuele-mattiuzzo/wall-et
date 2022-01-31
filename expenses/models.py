from django.db import models

from expenses.const import *


class Expense(models.Model):
    category = models.CharField(max_length=200,
                                choices=EXPENSE_CATEGORIES,
                                default='other')
    expense_type = models.CharField(max_length=200,
                                    choices=EXPENSE_TYPES,
                                    default='out')
    recurring = models.BooleanField(default=False)
    recurring_type = models.CharField(max_length=200,
                                      choices=RECURRING_TYPES,
                                      default='one-off')
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    date = models.DateField()

    def __str__(self):
        return '{} : "{}"'.format(self.date, self.name)
