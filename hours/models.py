from django.db import models
from django.urls import reverse
from django.utils import timezone


class Month(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tb_month', kwargs={'slug': self.slug})


class Shift(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class WorkDays(models.Model):
    date = models.DateField('Date', default=timezone.now, auto_now=False, null=True)
    month = models.ForeignKey(Month,
                              related_name='work_days',
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Month'
                              )
    slug = models.SlugField(max_length=50, unique=True)
    shift = models.ForeignKey(Shift,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name='work_days',
                              verbose_name='Смена')
    day = models.IntegerField(default=0, verbose_name='Кибон')
    night = models.IntegerField(default=0, verbose_name='Ночные')
    overtime = models.IntegerField(default=0, verbose_name='Чаноб')
    holiday_pay = models.IntegerField(default=0, verbose_name='Тыкын')
    holiday_overtime_pay = models.IntegerField(default=0, verbose_name='Тыкын-чаноб')
    parking_allowance = models.IntegerField(default=0, verbose_name='Парковка')

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['date']
