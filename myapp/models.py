from django.db import models

class MyApp(models.Model):
    name = models.CharField('Name', max_length = 200)
    surname = models.CharField('Surname', max_length = 200)
    age = models.IntegerField('Age', default=None)
    status = models.BooleanField('Status', default=True)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'