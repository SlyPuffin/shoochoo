from django.views.generic import ListView, DetailView
from .models import TaskItem

# Create your views here.
class TaskListView(ListView):
    model = TaskItem
    template_name = "home.html"

class TaskDetailView(DetailView):
    model = TaskItem
    template_name = "task_detail.html"
