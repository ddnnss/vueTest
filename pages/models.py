from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField('Название ', max_length=255, blank=True, null=True)
    price = models.IntegerField('Цена', blank=True, default=0, db_index=True)
    num = models.IntegerField(default=0)
