from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task', 'isCompleted', 'user',
                  'priority', 'created_at', 'updated_at']
