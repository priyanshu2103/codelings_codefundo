from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Volunteer

admin.site.register(Volunteer)

# class ProfileInline(admin.StackedInline):
#     model = Volunteer
#     can_delete = False
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = [ProfileInline]
#
#
# # unregister old user admin
# admin.site.unregister(User)
# # register new user admin
# admin.site.register(User, UserAdmin)
