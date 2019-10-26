from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Extend.forms import CustomUserCreationForm , CustomUserChangeForm
from Extend.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
