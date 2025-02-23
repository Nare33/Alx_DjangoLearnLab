from django.contrib import admin
from .models import UserProfile
from relationship_app.models import UserProfile

admin.site.register(UserProfile)

