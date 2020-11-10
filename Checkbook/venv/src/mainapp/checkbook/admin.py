from django.contrib import admin

# Register your models here.

from .models import Transaction, Account

admin.site.register(Transaction)

admin.site.register(Account)