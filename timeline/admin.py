from django.contrib import admin
from .models import Timeline,Comment
# Register your models here.
admin.site.register(Comment)

@admin.register(Timeline)
class timelineadmin(admin.ModelAdmin):
    list_display=["title","author","date"]
    list_display_links=["title","date"]
    search_fields=["title"]
    list_filter=["date"]
    class Meta:
        model=Timeline