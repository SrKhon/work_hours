from django.contrib import admin
from .models import Shift, WorkDays, Month, Rate


class RateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('rate_st',)}


class MonthAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class WorkDaysAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('date',)}
    list_display = ('date', 'shift', 'month')


class ShiftAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Shift, ShiftAdmin)
admin.site.register(WorkDays, WorkDaysAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Rate, RateAdmin)

