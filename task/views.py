from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task.models import Task
from task.serializers import TaskSerializer


@api_view(["GET"])
def home_view(request):
    http_enpoinds = {
        "root-page": "http://127.0.0.1:8000/",
        "task-list": "http://127.0.0.1:8000/tasks/list/",
        "task-create": "http://127.0.0.1:8000/tasks/create/",
        "task-detail": "http://127.0.0.1:8000/tasks/<task-id>/",
        "task-update": "http://127.0.0.1:8000/tasks/update/<task-id>/",
        "task-delete": "http://127.0.0.1:8000/tasks/delete/<task-id>/",
    }
    return Response(http_enpoinds, status=status.HTTP_200_OK)


@api_view(["GET"])
def todo_list_view(request):
    task_qs = Task.objects.all()
    task = TaskSerializer(task_qs, many=True)
    return Response(task.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_task_view(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": serializer.data, "status": status.HTTP_201_CREATED})
    return Response(
        {"error": "Sorry don't create and todo.", "status": status.HTTP_400_BAD_REQUEST}
    )


@api_view(["GET"])
def todo_detail_view(request, **kwargs):
    try:
        task_qs = Task.objects.get(pk=kwargs["pk"])
        serializer = TaskSerializer(task_qs, many=False)
        return Response({"success": serializer.data, "status": status.HTTP_200_OK})
    except Task.DoesNotExist:
        return Response(
            {
                "error": "Does Not Fount Your Task...",
                "status": status.HTTP_404_NOT_FOUND,
            }
        )


@api_view(["PUT"])
def todo_update_view(request, **kwargs):
    task_qs = Task.objects.get(pk=kwargs["pk"])
    serializer = TaskSerializer(task_qs, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def todo_delete_view(request, **kwargs):
    task_qs = Task.objects.get(pk=kwargs["pk"])
    task_qs.delete()
    return Response({"status": status.HTTP_204_NO_CONTENT})
