from django.shortcuts import render
from django.db.models import *
from .models import WorkDays, Month


def days(request):
    months = Month.objects.all()  # To list the months in menu navbar
    work_days = WorkDays.objects.all()

    sum_hours_day = WorkDays.objects.aggregate(Sum('day'))
    sum_hours_night = WorkDays.objects.aggregate(Sum('night'))
    sum_hours_overtime = WorkDays.objects.aggregate(Sum('overtime'))
    sum_hours_holiday_pay = WorkDays.objects.aggregate(Sum('holiday_pay'))
    sum_hours_holiday_overtime_pay = WorkDays.objects.aggregate(Sum('holiday_overtime_pay'))
    sum_hours_parking_allowance = WorkDays.objects.aggregate(Sum('parking_allowance'))

    context = {
        'work_days': work_days,
        'months': months,
        'sum_hours_day': sum_hours_day['day__sum'],
        'sum_hours_night': sum_hours_night['night__sum'],
        'sum_hours_overtime': sum_hours_overtime['overtime__sum'],
        'sum_hours_holiday_pay': sum_hours_holiday_pay['holiday_pay__sum'],
        'sum_hours_holiday_overtime_pay': sum_hours_holiday_overtime_pay['holiday_overtime_pay__sum'],
        'sum_hours_parking_allowance': sum_hours_parking_allowance['parking_allowance__sum'],
    }
    return render(request, 'hours/index.html', context)


def tbl_month(request, slug):
    months = Month.objects.all()  # To list the months in menu navbar
    current_month = Month.objects.get(slug__iexact=slug)

    sum_hours_day = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('day'))
    sum_hours_night = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('night'))
    sum_hours_overtime = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('overtime'))
    sum_hours_holiday_pay = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('holiday_pay'))
    sum_hours_holiday_overtime_pay = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('holiday_overtime_pay'))
    sum_hours_parking_allowance = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('parking_allowance'))

    context = {
        'current_month': current_month,
        'months': months,
        'sum_hours_day': sum_hours_day['day__sum'],
        'sum_hours_night': sum_hours_night['night__sum'],
        'sum_hours_overtime': sum_hours_overtime['overtime__sum'],
        'sum_hours_holiday_pay': sum_hours_holiday_pay['holiday_pay__sum'],
        'sum_hours_holiday_overtime_pay': sum_hours_holiday_overtime_pay['holiday_overtime_pay__sum'],
        'sum_hours_parking_allowance': sum_hours_parking_allowance['parking_allowance__sum'],
    }
    return render(request, 'hours/get_month.html', context)
