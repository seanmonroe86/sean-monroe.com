from django.db import models

class NavItem(models.Model):
    name = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    index = models.IntegerField(default = 0)

class Account(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 256)
    acct_lvl = models.CharField(max_length = 10,
                                default = 'user')

