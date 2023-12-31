from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class TaskTag(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class TaskItem(models.Model):
    DUE = 'DUE'
    COMPLETE = 'COMPLETE'
    OVERDUE = 'OVERDUE'
    STATUS = (
        (DUE, DUE),
        (COMPLETE, COMPLETE),
        (OVERDUE, OVERDUE)
    )
    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField(null=True, blank=True)
    due_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS, default=DUE)
    estimated_time = models.IntegerField(default=15)
    elapsed_time = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=TaskTag, related_name="tasks", blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})

    def complete(self):
        self.status = 'COMPLETE'
        self.due_date = timezone.datetime.today()
        self.save(update_fields=["status", "due_date"])