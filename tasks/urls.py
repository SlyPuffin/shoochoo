from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("task/new/", TaskCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit"),
    path("", TaskListView.as_view(), name="home"),
]
