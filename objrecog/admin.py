from django.contrib import admin
from .models import RecordListDB

# Customize Admin Panel
admin.site.site_header = "Home Security Admin Panel"
admin.site.site_title = "Home Security"

# Register your models here.
admin.site.register(RecordListDB)