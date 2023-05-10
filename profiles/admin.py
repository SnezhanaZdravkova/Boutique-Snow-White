from django.contrib import admin

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'default_phone_number',
    )


admin.site.register(UserProfile, ProfileAdmin)
