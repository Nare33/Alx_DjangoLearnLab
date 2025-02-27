from django.contrib.auth.models import Group, Permission
from .models import Article
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

def create_groups_and_permissions():
    editors_group, created = Group.objects.get_or_create(name='Editors')
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    admins_group, created = Group.objects.get_or_create(name='Admins')

    can_view_perm = Permission.objects.get(codename='can_view')
    can_create_perm = Permission.objects.get(codename='can_create')
    can_edit_perm = Permission.objects.get(codename='can_edit')
    can_delete_perm = Permission.objects.get(codename='can_delete')

    editors_group.permissions.set([can_create_perm, can_edit_perm])
    viewers_group.permissions.set([can_view_perm])
    admins_group.permissions.set([can_view_perm, can_create_perm, can_edit_perm, can_delete_perm])
    
    editors_group.save()
    viewers_group.save()
    admins_group.save()


