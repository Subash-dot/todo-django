from django.contrib import admin
from TodoApp.models import Todo



class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'deadline', 'created_at')
    list_filter = ('title', 'description', 'completed', 'deadline', 'created_at')
    search_fields = ('title', 'description', 'completed', 'deadline', 'created_at')
    ordering = ['title']

admin.site.register(Todo, TodoAdmin)

