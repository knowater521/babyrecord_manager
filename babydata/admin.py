from django.contrib import admin
from .models import DrinkMilk, Pee, Sleep, BreastBump


# Register your models here.

class DrinkMilkAdmin(admin.ModelAdmin):
    list_display = ('drink_at', 'amount', 'drink_type', 'record_at')
    ordering = ('drink_at',)

class PeeAdmin(admin.ModelAdmin):
    list_display = ('record_date', 'pee_type', 'amount', 'record_at')
    ordering = ('record_date',)

class SleepAdmin(admin.ModelAdmin):
    list_display = ('sleep_start', 'sleep_end', 'record_at')
    ordering = ('sleep_start',)

class BreastBumpAdmin(admin.ModelAdmin):
    list_display = ('bump_at', 'amount', 'record_at')
    ordering = ('bump_at',)


admin.site.register(DrinkMilk, DrinkMilkAdmin)
admin.site.register(Pee, PeeAdmin)
admin.site.register(Sleep, SleepAdmin)
admin.site.register(BreastBump, BreastBumpAdmin)