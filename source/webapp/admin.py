from django.contrib import admin
from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'to_do_date']
    list_display_links = ['title']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['title', 'description', 'status', 'to_do_date']

admin.site.register(Task, TaskAdmin)