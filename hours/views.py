from django.shortcuts import render
from django.db.models import *
from .models import WorkDays, Month


def days(request):
    work_days = WorkDays.objects.all()
    months = Month.objects.all()
    sum_hours_day = WorkDays.objects.aggregate(Day=Sum('day'))
    sum_hours_night = WorkDays.objects.aggregate(Night=Sum('night'))
    sum_hours_overtime = WorkDays.objects.aggregate(Overtime=Sum('overtime'))
    sum_hours_holiday_pay = WorkDays.objects.aggregate(Holiday_pay=Sum('holiday_pay'))
    sum_hours_holiday_overtime_pay = WorkDays.objects.aggregate(Holiday_overtime_pay=Sum('holiday_overtime_pay'))
    sum_hours_parking_allowance = WorkDays.objects.aggregate(Parking_allowance=Sum('parking_allowance'))
    context = {
        'work_days': work_days,
        'months': months,
        'sum_hours_day': sum_hours_day['Day'],
        'sum_hours_night': sum_hours_night['Night'],
        'sum_hours_overtime': sum_hours_overtime['Overtime'],
        'sum_hours_holiday_pay': sum_hours_holiday_pay['Holiday_pay'],
        'sum_hours_holiday_overtime_pay': sum_hours_holiday_overtime_pay['Holiday_overtime_pay'],
        'parking_allowance': sum_hours_parking_allowance['Parking_allowance'],
    }
    return render(request, 'hours/index.html', context)


def tbl_month(request, slug):
    months = Month.objects.all()  # To list the months in menu navbar
    hours = WorkDays.objects.filter(month__slug=slug)  # To display class fields end current month
    sum_hours_day = WorkDays.objects.filter(month__slug=slug).aggregate(Day=Sum('day'))
    sum_hours_night = WorkDays.objects.filter(month__slug=slug).aggregate(Night=Sum('night'))
    sum_hours_overtime = WorkDays.objects.filter(month__slug=slug).aggregate(Overtime=Sum('overtime'))
    sum_hours_holiday_pay = WorkDays.objects.filter(month__slug=slug).aggregate(Holiday_pay=Sum('holiday_pay'))
    sum_hours_holiday_overtime_pay = WorkDays.objects.filter(month__slug=slug).aggregate(Holiday_overtime_pay=Sum('holiday_overtime_pay'))
    sum_hours_parking_allowance = WorkDays.objects.filter(month__slug=slug).aggregate(Parking_allowance=Sum('parking_allowance'))
    context = {
        'hours': hours,
        'months': months,
        'sum_hours_day': sum_hours_day['Day'],
        'sum_hours_night': sum_hours_night['Night'],
        'sum_hours_overtime': sum_hours_overtime['Overtime'],
        'sum_hours_holiday_pay': sum_hours_holiday_pay['Holiday_pay'],
        'sum_hours_holiday_overtime_pay': sum_hours_holiday_overtime_pay['Holiday_overtime_pay'],
        'parking_allowance': sum_hours_parking_allowance['Parking_allowance'],
    }
    return render(request, 'hours/get_month.html', context)
