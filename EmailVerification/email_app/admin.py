from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    UserAdmin.fieldsets += (
        ("User Activation Info", {"fields": ("is_verified", "is_send_email")}),
    )
    # list_display = ('email','is_staff', 'is_active')
    # list_filter = ('email', 'is_staff', 'is_active')
    # fieldsets = (
    #     (
    #         "Personal Info",
    #         {
    #             "fields":(
    #                 "first_name",
    #                 "last_name",
    #                 "email",
    #             ),
    #         }
    #     ),
    # )
    search_fields = ('email',)
    
admin.site.register(User, UserAdmin)
