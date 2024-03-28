from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = ((True, "Done"), (False, "Not done"))
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-status", "created"]
