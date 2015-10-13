from django.contrib import admin
from log_errors.models import Log_Errors

class Log_ErrorsDetails(admin.ModelAdmin):
    list_display = ("error_human", "date_time")
    ordering = ['-date_time']


admin.site.register(Log_Errors,Log_ErrorsDetails)