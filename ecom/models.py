# models.py
from django.db import models

class Registration2(models.Model):
    # id = models.CharField(max_length=60)
    userName = models.CharField(max_length=60)
    emailId = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    regType = models.CharField(max_length=1)
    loginToken = models.CharField(max_length=5, default=00000)
    
    def __str__(self):
        return self.userName
        # return f'{self.userName}, {self.emailId}, {self.password}, {self.regType}'


class Items(models.Model):
    
    itemName = models.CharField(max_length=60)
    itemNo = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    cost = models.CharField(max_length=60)

    def __str__(self):
        return self.itemName


class OrderHistory(models.Model):
    userName = models.CharField(max_length=60)
    emailId = models.CharField(max_length=60)
    itemName = models.CharField(max_length=60)
    itemNo = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    cost = models.CharField(max_length=60)
    
    def __str__(self):
        return self.itemName