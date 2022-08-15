from django.contrib import admin
from .models import *

@admin.register(Food)
class Food_Admin(admin.ModelAdmin):
    list_display = ('name','price','description','image',)



