from django.shortcuts import render
from .models import WorkDays, Month


def days(request):
    work_days = WorkDays.objects.all()
    months = Month.objects.all()
    return render(request, 'hours/index.html', {'work_days': work_days, 'months': months})


def tb_month(request, slug):
    months = Month.objects.all()
    month = Month.objects.get(slug__iexact=slug)
    return render(request, 'hours/get_month.html', {'month': month, 'months': months})



