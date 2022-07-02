from django.db import models

# Create your models here.


class Todo(models.Model):
    # create a foreign key to the user model
    task = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.task
