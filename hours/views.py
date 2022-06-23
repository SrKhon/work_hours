from django.shortcuts import render
from django.db.models import *
from .models import WorkDays, Month, Rate


def days(request):
    work_days = WorkDays.objects.all()
    rate = Rate.objects.get(id=1)

    sum_hours_day = WorkDays.objects.aggregate(Sum('day'))
    sum_hours_night = WorkDays.objects.aggregate(Sum('night'))
    sum_hours_overtime = WorkDays.objects.aggregate(Sum('overtime'))
    sum_hours_holiday_pay = WorkDays.objects.aggregate(Sum('holiday_pay'))
    sum_hours_holiday_overtime_pay = WorkDays.objects.aggregate(Sum('holiday_overtime_pay'))
    sum_hours_parking_allowance = WorkDays.objects.aggregate(Sum('parking_allowance'))

    day_hours_pay = sum_hours_day['day__sum'] * rate.rate_st

    context = {
        'day_hours_pay': day_hours_pay,
        'work_days': work_days,
        'sum_hours_day': sum_hours_day['day__sum'],
        'sum_hours_night': sum_hours_night['night__sum'],
        'sum_hours_overtime': sum_hours_overtime['overtime__sum'],
        'sum_hours_holiday_pay': sum_hours_holiday_pay['holiday_pay__sum'],
        'sum_hours_holiday_overtime_pay': sum_hours_holiday_overtime_pay['holiday_overtime_pay__sum'],
        'sum_hours_parking_allowance': sum_hours_parking_allowance['parking_allowance__sum'],
    }
    return render(request, 'hours/index.html', context)


def tbl_month(request, slug):
    current_month = Month.objects.get(slug__iexact=slug)

    sum_hours_day = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('day'))
    sum_hours_night = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('night'))
    sum_hours_overtime = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('overtime'))
    sum_hours_holiday_pay = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('holiday_pay'))
    sum_hours_holiday_overtime_pay = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('holiday_overtime_pay'))
    sum_hours_parking_allowance = WorkDays.objects.filter(month__slug=slug).aggregate(Sum('parking_allowance'))

    day_hours_pay = sum_hours_day['day__sum'] * current_month.rate.rate_st
    overtime_hours_pay = sum_hours_overtime['overtime__sum'] * current_month.rate.rate_st * (150 / 100)
    night_hours_pay = sum_hours_night['night__sum'] * current_month.rate.rate_st * (50 / 100)
    holiday_hours_pay = sum_hours_holiday_pay['holiday_pay__sum'] * current_month.rate.rate_st * (150 / 100)
    holiday_overtime_hours_pay = sum_hours_holiday_overtime_pay['holiday_overtime_pay__sum'] * current_month.rate.rate_st * (200 / 100)
    parking_allowance = 0.0
    annual_allowance = 73280

    context = {
        'current_month': current_month,

        'day_hours_pay': day_hours_pay,
        'overtime_hours_pay': overtime_hours_pay,
        'night_hours_pay': night_hours_pay,
        'holiday_hours_pay': holiday_hours_pay,
        'holiday_overtime_hours_pay': holiday_overtime_hours_pay,
        'parking_allowance': parking_allowance,
        'annual_allowance': annual_allowance,

        'sum_hours_day': sum_hours_day['day__sum'],
        'sum_hours_overtime': sum_hours_overtime['overtime__sum'],
        'sum_hours_night': sum_hours_night['night__sum'],
        'sum_hours_holiday_pay': sum_hours_holiday_pay['holiday_pay__sum'],
        'sum_hours_holiday_overtime_pay': sum_hours_holiday_overtime_pay['holiday_overtime_pay__sum'],
        'sum_hours_parking_allowance': sum_hours_parking_allowance['parking_allowance__sum'],
    }
    return render(request, 'hours/get_month.html', context)
