from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=40, help_text="Project title")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="Start time")
    completion_time = models.DateTimeField(null=True, help_text="End time")

    def __str__(self):
        return self.title


class Task(models.Model):
    """Activity to be completed"""

    activity = models.CharField(max_length=40, help_text="Title the activity")
    description = models.TextField(help_text="More information on activity to partake")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_estimate = models.IntegerField(
        help_text="Time in hours required to compelete activity"
    )
    completed = models.BooleanField(default=False, help_text="Task completion status")

    def __str__(self):
        return self.activity
