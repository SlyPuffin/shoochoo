from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import TaskItem

# Create your views here.
class TaskListView(ListView):
    model = TaskItem
    template_name = "home.html"

class TaskDetailView(DetailView):
    model = TaskItem
    template_name = "task_detail.html"

class TaskCreateView(CreateView):
    model = TaskItem
    template_name = "task_new.html"
    fields = ["title", "author", "body", "estimated_time", "due_date"]
