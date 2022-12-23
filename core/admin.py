from django.contrib import admin
from .models import *

class UserdateAdmin(admin.ModelAdmin):
    list_display = ['user','date']
admin.site.register(Userdate, UserdateAdmin)

class UsernoteAdmin(admin.ModelAdmin):
    list_display = ['userdate','time','task','isdone']
admin.site.register(Usernote, UsernoteAdmin)

 