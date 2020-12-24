from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


@admin.register(models.User)
# 클래스 아래에 admin.site.register(models.User, CustomUserAdmin)를 추가했을 때도 동일하게 동작
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    # list_display = ('username', 'email', 'gender',
    #                 'language', 'currency', 'superhost')
    # list_filter = ('language', 'currency', 'superhost',)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )
