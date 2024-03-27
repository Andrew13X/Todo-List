from django.contrib import admin

from catalog.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("tags", "status", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
