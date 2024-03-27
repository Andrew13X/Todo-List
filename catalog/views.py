from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from catalog.models import Tag, Task
from catalog.forms import TaskForm


class IndexView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "catalog/index.html"
    queryset = Task.objects.all()


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:index")


def toggle_complete_undo(request, pk):
    task = Task.objects.get(id=pk)
    if task.status == "Done":
        task.status = "Not done"
        task.save()
    elif task.status == "Not done":
        task.status = "Done"
        task.save()
    return HttpResponseRedirect(reverse_lazy("catalog:index"))
