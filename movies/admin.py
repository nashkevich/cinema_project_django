from django.contrib import admin
from .models import Movie
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Movie._meta.get_fields()]