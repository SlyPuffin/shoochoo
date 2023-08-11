from django.urls import path
from . import views

urlpatterns = [
    path("task/new/", views.TaskCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/focus", views.TaskFocusView.as_view(), name="task_focus"),
    path("task/<int:pk>/edit", views.TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete", views.TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/complete", views.task_complete, name="task_complete"),
    path("", views.TaskListView.as_view(), name="home"),
]
