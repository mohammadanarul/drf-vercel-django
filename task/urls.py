from django.urls import path

from .views import (
    create_task_view,
    todo_delete_view,
    todo_detail_view,
    todo_list_view,
    todo_update_view,
)

urlpatterns = [
    path("list/", todo_list_view, name="tasks"),
    path("create/", create_task_view, name="task-create"),
    path("<pk>/", todo_detail_view, name="task_detail"),
    path("update/<pk>/", todo_update_view, name="task_update"),
    path("delete/<pk>/", todo_delete_view, name="task_delete"),
]
