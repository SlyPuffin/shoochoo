from django import forms
from .models import TaskItem

class TaskCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["body"].widget.attrs.update({"class": "form-control h-25"})
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        self.fields["estimated_time"].widget.attrs.update({"class": "form-control"})
        self.fields["due_date"].widget.attrs.update({"class": "form-control"})
    class Meta:
        model = TaskItem
        fields = ["title", "body", "status", "estimated_time", "due_date"]

class TaskUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["body"].widget.attrs.update({"class": "form-control h-25"})
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        self.fields["elapsed_time"].widget.attrs.update({"class": "form-control"})
        self.fields["estimated_time"].widget.attrs.update({"class": "form-control"})
        self.fields["due_date"].widget.attrs.update({"class": "form-control"})
    class Meta:
        model = TaskItem
        fields = ["title", "body", "status", "elapsed_time", "estimated_time", "due_date"]
