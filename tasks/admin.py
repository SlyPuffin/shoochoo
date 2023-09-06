from django.contrib import admin
from .models import TaskItem, TaskTag

# Register your models here.
admin.site.register(TaskItem)
admin.site.register(TaskTag)
