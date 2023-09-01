from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
from .models import TaskItem
from .forms import TaskUpdateForm, TaskCreateForm
from django.utils import timezone
from django.db.models import Q

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
    template_name = "home.html"

    def get_queryset(self):
        today = timezone.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        objects = TaskItem.objects.filter(author=self.request.user).extra(select={"status_order":"case when status='OVERDUE' then 0 when status = 'DUE' then 1 else 2 end"}).order_by('due_date', 'status_order').exclude(~Q(due_date=today), status='COMPLETE')#.filter(~Q(status='COMPLETE', due_date__lt=today))#.filter(status='DUE')
        for obj in objects:
            if obj.due_date < today.date() and obj.status == 'DUE':
                obj.status = 'OVERDUE'
                obj.save()
            elif obj.due_date >= today.date() and obj.status == 'OVERDUE':
                obj.status = 'DUE'
                obj.save()

        objects = objects.annotate(due_today=Q(due_date=today.date()) & Q(status='DUE'))
        return objects

#.filter(due_date__gte=today)

class CompletedTaskListView(LoginRequiredMixin, ListView):
    template_name = "completed.html"

    def get_queryset(self):
        objects = TaskItem.objects.filter(author=self.request.user).filter(status='COMPLETE')
        return objects

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
