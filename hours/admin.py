from django.contrib import admin
from .models import Shift, WorkDays



class WorkDaysAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('date',)}



class ShiftAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Shift, ShiftAdmin)
admin.site.register(WorkDays, WorkDaysAdmin)

