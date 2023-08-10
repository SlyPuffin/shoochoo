from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskFocusView

urlpatterns = [
    path("task/new/", TaskCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/focus", TaskFocusView.as_view(), name="task_focus"),
    path("task/<int:pk>/edit", TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("", TaskListView.as_view(), name="home"),
]
