from django.shortcuts import render
from django.db.models import *
from .models import WorkDays, Month


def days(request):
    work_days = WorkDays.objects.all()
    months = Month.objects.all()
    sum_hours = WorkDays.objects.aggregate(Day=Sum('day'))
    context = {'work_days': work_days, 'months': months, 'sum_hours': sum_hours['Day']}
    return render(request, 'hours/index.html', context)


def tbl_month(request, slug):
    months = Month.objects.all()
    month = WorkDays.objects.filter(month__slug=slug)
    sum_hours_day = WorkDays.objects.filter(month__slug=slug).aggregate(Day=Sum('day'))
    sum_hours_night = WorkDays.objects.filter(month__slug=slug).aggregate(Night=Sum('night'))
    sum_hours_overtime = WorkDays.objects.filter(month__slug=slug).aggregate(Overtime=Sum('overtime'))
    context = {
        'month': month,
        'months': months,
        'sum_hours_day': sum_hours_day['Day'],
        'sum_hours_night': sum_hours_night['Night'],
        'sum_hours_overtime': sum_hours_overtime['Overtime'],
    }
    return render(request, 'hours/get_month.html', context)
