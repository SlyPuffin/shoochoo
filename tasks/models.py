from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class TaskItem(models.Model):
    DUE = 'DUE'
    FORREVIEW = 'FORREVIEW'
    RESTING = 'RESTING'
    RESCHEDULED = 'RESCHEDULED'
    STATUS = (
        (DUE, DUE),
        (FORREVIEW, FORREVIEW),
        (RESTING, RESTING),
        (RESCHEDULED, RESCHEDULED)
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField(null=True, blank=True)
    due_date = models.DateField(default=timezone.now)
    task_finished = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=STATUS, default=DUE)
    estimated_time = models.IntegerField()
    elapsed_time = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
