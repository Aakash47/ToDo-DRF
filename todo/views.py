from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from .serializers import TodoSerializers
from .models import Todo

# Create your views here.


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)


@extend_schema(responses=TodoSerializers)
@api_view(['GET'])
def todo(request):
    task = Todo.objects.all()
    serializer = TodoSerializers(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tododetail(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializers(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def todocreate(request):
    serializer = TodoSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def todoupdate(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializers(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def tododelete(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response("Task deleted Successfully")
