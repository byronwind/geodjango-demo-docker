from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Country
from .models import WorldBorder

admin.site.register(WorldBorder, admin.ModelAdmin)