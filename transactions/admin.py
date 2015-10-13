from django.contrib import admin
from transactions.models import Transaction

class TransactionDetails(admin.ModelAdmin):
    list_display = ("folio_android", "send", "status", "response", "date_time")
    ordering = ['-date_time']

admin.site.register(Transaction,TransactionDetails)

