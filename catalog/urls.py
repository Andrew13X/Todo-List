from django.urls import path

from catalog.views import (
    IndexView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TagDeleteView,
    TaskUpdateView,
    ToggleCompleteUndo
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/toggle-complete-undo/",
        ToggleCompleteUndo.as_view(),
        name="toggle-complete-undo"
    )
]

app_name = "catalog"
