from django import forms # type: ignore
from django.utils import timezone # type: ignore
from django.core.exceptions import ValidationError # type: ignore
from .models import Task

class CustomTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título da tarefa',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição detalhada',
                'rows': 4,
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')

        if due_date <= timezone.now():
            raise ValidationError("A data de prazo não pode ser no passado.")
        return due_date

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        