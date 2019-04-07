from django.contrib import admin
from .models import images



class AdminImages(admin.ModelAdmin):
    list_display = ['id_no','name','loc','image','profile']

admin.site.register(images,AdminImages)