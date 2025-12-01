from django.db import models

# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField()
    Date_Created = models.DateTimeField(auto_now_add=True)
    Is_Done = models.BooleanField()
    def __str__(self):
        return self.Title
