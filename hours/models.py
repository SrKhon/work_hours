from django.db import models
from django.utils import timezone


class Shift(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class WorkDays(models.Model):
    date = models.DateField('Дата', default=timezone.now, auto_now=False, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, related_name='work_days', verbose_name='Смена')
    day = models.IntegerField(default=0, verbose_name='Кибон')
    night = models.IntegerField(default=0, verbose_name='Ночные')
    overtime = models.IntegerField(default=0, verbose_name='Чаноб')
    holyday_work = models.IntegerField(default=0, verbose_name='Тыкын')

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['date']
