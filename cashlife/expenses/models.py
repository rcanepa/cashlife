from django.contrib.auth.models import User
from django.db import models

from categories.models import Category

class Expense(models.Model):
    detail = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    created_by = models.ForeignKey(User, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.detail

