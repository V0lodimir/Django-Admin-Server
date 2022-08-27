from django.db import models

class MyApps(models.Model):
    car = models.CharField('Car', max_length = 200)
    model = models.CharField('Model', max_length = 200)

    def __str__(self):
        return self.car + " " + self.model

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'