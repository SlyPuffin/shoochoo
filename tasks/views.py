from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import TaskItem
from .forms import TaskUpdateForm, TaskCreateForm


# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    #model = TaskItem
    template_name = "home.html"

    def get_queryset(self):
        return TaskItem.objects.filter(author=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = TaskItem
    template_name = "task_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TaskFocusView(LoginRequiredMixin, DetailView):
    model = TaskItem
    template_name = "task_focus.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TaskItem
    template_name = "task_new.html"
    form_class = TaskCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TaskItem
    template_name = "task_edit.html"
    form_class = TaskUpdateForm

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TaskItem
    template_name = "task_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
