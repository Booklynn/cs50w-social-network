from django.contrib import admin

from .models import User, Follow

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    user_display = ("username", "first_name")

class FollowAdmin(admin.ModelAdmin):
    follow_display = ("follower", "followed", "created_at")

admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
