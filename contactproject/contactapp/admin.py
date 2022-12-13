from django.contrib import admin
from .models import Category, Profile, QrCode
# Register your models here.


admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(QrCode)