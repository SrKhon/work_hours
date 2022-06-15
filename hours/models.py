from django.db import models
from django.urls import reverse
from django.utils import timezone


class Rate(models.Model):
    rate_st = models.IntegerField(default=9160)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.rate_st)


class Month(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tbl_month', kwargs={'slug': self.slug})


class Shift(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class WorkDays(models.Model):
    date = models.DateField('Дата', default=timezone.now, auto_now=False, null=True)
    month = models.ForeignKey(
        Month,
        on_delete=models.SET_NULL,
        null=True,
        related_name='work_days',
        verbose_name='Месяц'
    )
    slug = models.SlugField(max_length=50, unique=True)
    shift = models.ForeignKey(
        Shift,
        on_delete=models.SET_NULL,
        null=True,
        related_name='work_days',
        verbose_name='Смена')
    day = models.FloatField(default=0, verbose_name='Стандартный день')
    night = models.FloatField(default=0, verbose_name='Ночные')
    overtime = models.FloatField(default=0, verbose_name='Сверхурочные')
    holiday_pay = models.FloatField(default=0, verbose_name='Работа в выходые')
    holiday_overtime_pay = models.FloatField(default=0, verbose_name='Сверхурочные в выходые')
    parking_allowance = models.FloatField(default=0, verbose_name='Парковка')
    rate = models.ForeignKey(
        Rate,
        on_delete=models.SET_NULL,
        null=True,
        default=0,
        related_name='work_days',
        verbose_name='Ставка',
    )

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['date']
