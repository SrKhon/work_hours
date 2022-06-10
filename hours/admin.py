from django.contrib import admin
from .models import Shift, WorkDays, Month


class MonthAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class WorkDaysAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('date',)}


class ShiftAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Shift, ShiftAdmin)
admin.site.register(WorkDays, WorkDaysAdmin)
admin.site.register(Month, MonthAdmin)

