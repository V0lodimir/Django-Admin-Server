from django.db import models

class MyApp2(models.Model):
    mobile = models.CharField('Mobile', max_length = 200)
    model = models.CharField('Model', max_length = 200)

    def __str__(self):
        return self.mobile + " " + self.model

    class Meta:
        verbose_name = 'mobile'
        verbose_name_plural = 'mobiles'
