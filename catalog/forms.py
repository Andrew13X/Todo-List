from django import forms

from catalog.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"rows": 2})
        }
