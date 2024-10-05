from django.contrib import admin
from .models import user_model

# Register your models here.
class user_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password', 'textbox')
    
admin.site.register(user_model, user_admin)
