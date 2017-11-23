from django.db import models

class NavItem(models.Model):
    name = models.CharField(max_length = 200)
    url = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    index = models.IntegerField(default = 0)


