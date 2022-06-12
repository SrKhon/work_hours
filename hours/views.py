from django.shortcuts import render
from django.db.models import *
from .models import WorkDays, Month


def days(request):
    work_days = WorkDays.objects.all()
    months = Month.objects.all()
    hours_month = WorkDays.objects.aggregate(Day=Sum('day'))
    context = {'work_days': work_days, 'months': months, 'hours_month': hours_month['Day']}
    return render(request, 'hours/index.html', context)


def tb_month(request, slug):
    months = Month.objects.all()
    month = WorkDays.objects.filter(month__slug=slug)
    sum_hours = WorkDays.objects.filter(month__slug=slug).aggregate(Day=Sum('day'))
    context = {'month': month, 'months': months, 'sum_hours': sum_hours['Day']}
    return render(request, 'hours/get_month.html', context)



