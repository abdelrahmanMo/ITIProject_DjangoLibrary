from django.contrib import admin
from .models import Books,Authors,status
# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(statusName=1)
make_published.short_description = "Mark selected books as published"

class BookAdmin(admin.ModelAdmin):
    #list_filter = ['created','active']
    list_display = ['Name','statusName']
    search_fields = ['Name']
    actions = [make_published]
admin.site.register(Books,BookAdmin)
admin.site.register(Authors)
admin.site.register(status)