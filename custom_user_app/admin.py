from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import CustomUser


# Define an inline admin descriptor for CustomUser model
# which acts a bit like a singleton
class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "custom users"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [CustomUserInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
