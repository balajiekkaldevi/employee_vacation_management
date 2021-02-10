from django.contrib import admin
from .models import employee,manager,days
# Register your models here.
@admin.register(employee)
@admin.register(manager)
@admin.register(days)
class ad(admin.ModelAdmin):
    pass