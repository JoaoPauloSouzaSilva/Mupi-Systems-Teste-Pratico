from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  due_date = models.DateTimeField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
