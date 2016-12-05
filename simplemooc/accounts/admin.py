from django.contrib import admin
from .models import User
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name', 'is_active', 'is_staff', 'date_joined')
    list_display_links = ('username', 'email', 'name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('username', 'email', 'name', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'name', 'is_active', 'is_staff', 'date_joined')
	
admin.site.register(User, UsuarioAdmin)