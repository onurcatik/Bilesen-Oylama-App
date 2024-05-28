from django.contrib import admin
from django.contrib.auth.models import User

def activate_user(modeladmin, request, queryset):
    queryset.update(is_active=True)

activate_user.short_description = 'Activate selected users'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff')
    actions = [activate_user]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
