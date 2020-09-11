from django.db import models


class FirstParametr(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Visualize(models.Model):
    type=models.CharField(max_length=20)

    def __str__(self):
        return  self.type


class SecondParametr(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name