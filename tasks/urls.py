from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path("task/new/", TaskCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("", TaskListView.as_view(), name="home"),
]
