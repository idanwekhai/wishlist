from django.db import models

# Create your models here.
class Wish(models.Model):
    name = models.CharField(max_length=150)
    sess_key = models.CharField(max_length=200, default="null")
    price = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'wish'
        verbose_name_plural = 'wishes'

