from django.contrib import admin
from .models import CareerCategory,CareerDetail,CareerPath, FAQ

# Register your models here.
admin.site.register(CareerCategory)
admin.site.register(CareerDetail)
admin.site.register(CareerPath)
admin.site.register(FAQ)