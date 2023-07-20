from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    fields = ["title", "author", "body", "status", "estimated_time", "due_date"]

class TaskUpdateView(UpdateView):
    model = TaskItem
    template_name = "task_edit.html"
    fields = ["title", "body", "status", "elapsed_time", "estimated_time", "due_date"]

class TaskDeleteView(DeleteView):
    model = TaskItem
    template_name = "task_delete.html"
    success_url = reverse_lazy("home")
