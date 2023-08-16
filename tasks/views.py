from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
from .models import TaskItem
from .forms import TaskUpdateForm, TaskCreateForm
from django.utils import timezone

def task_complete(request, pk):
    task = get_object_or_404(TaskItem, pk=pk)
    task.complete()
    refererUrl = request.META.get('HTTP_REFERER')
    if "focus" in refererUrl:
        return redirect("task_detail", pk=pk)
    else:
        return redirect(request.META.get('HTTP_REFERER', 'home'))

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    #model = TaskItem
    template_name = "home.html"

    def get_queryset(self):
        today = timezone.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        return TaskItem.objects.filter(author=self.request.user).filter(due_date__gte=today).extra(select={"status_order":"case when status='DUE' then 0 when status = 'COMPLETE' then 1 else 2 end"}).order_by('due_date', 'status_order')#.filter(status='DUE')


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
