from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year')
    list_filter = ('genre', 'release_year')
    search_fields = ('title', 'genre')