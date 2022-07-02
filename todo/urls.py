from django.conf.urls import url
from django.urls import path, include
from .views import (
    TodoDetailApiView,
    TodoListApiView,
)

urlpatterns = [
    path('', TodoListApiView.as_view()),
    path('<int:todo_id>/', TodoDetailApiView.as_view()),
]
