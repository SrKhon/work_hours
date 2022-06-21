from django.contrib import admin
from .models import Shift, WorkDays, Month, Rate


class RateAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'rate_st')
    prepopulated_fields = {'slug': ('rate_st',)}
    empty_value_display = '-empty-'


class MonthAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class WorkDaysAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    prepopulated_fields = {'slug': ('date',)}
    list_display = ('date', 'shift', 'month')
    readonly_fields = ('rate',)
    date_hierarchy = 'date'


class ShiftAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Shift, ShiftAdmin)
admin.site.register(WorkDays, WorkDaysAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Rate, RateAdmin)

