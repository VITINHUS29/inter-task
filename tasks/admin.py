from django.contrib import admin
from .models import Task, Category

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'completed', 'category')
    list_filter = ('completed', 'category', 'user')
    search_fields = ('title',)
    list_editable = ('completed',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Category)