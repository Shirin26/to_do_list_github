from django.contrib import admin
from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'to_do_date']
    list_display_links = ['description']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['id', 'description', 'status', 'to_do_date']

admin.site.register(Task, TaskAdmin)