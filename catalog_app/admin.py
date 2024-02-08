from django.contrib import admin

# Register your models here.
from .models import Product, Account, Transfer

admin.site.register(Product)
admin.site.register(Account)
admin.site.register(Transfer)

