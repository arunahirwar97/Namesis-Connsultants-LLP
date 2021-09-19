from django.contrib import admin

# Register your models here.
from .models import login_user
admin.site.register(login_user)