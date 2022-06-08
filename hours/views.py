from django.shortcuts import render
from .models import WorkDays


def days(request):
    work_days = WorkDays.objects.all()
    return render(request, 'hours/index.html', {'work_days': work_days})




