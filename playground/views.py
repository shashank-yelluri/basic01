from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Todos
from .serializers import TodosSerializer

@csrf_exempt
# Create your views here.
def health_check(request):
    return JsonResponse({
        "status": "success",
        "code": "200"
    })

@csrf_exempt
def todos(request, id=0):
    if request.method == "GET":
        todos = Todos.objects.all()
        todos_serializer = TodosSerializer(todos, many=True)
        return JsonResponse(todos_serializer.data, safe=False)
    
    elif request.method == "POST":
        todos_data = JSONParser().parse(request)
        # print(todos_data)
        todos_serializer = TodosSerializer(data=todos_data)
        if todos_serializer.is_valid():
            todos_serializer.save()
            return JsonResponse({
                "status": "Todo added !",
            })
        return JsonResponse({
                "status": "Failed to add !",
            })
    elif request.method == "PUT":
        todos_data = JSONParser().parse(request)
        todo = Todos.objects.get(name=todos_data['name'])
        todos_serializer = TodosSerializer(todo, data=todos_data)
        if todos_serializer.is_valid():
            todos_serializer.save()
            return JsonResponse({
                "status": "Todo updated !",
            })
        return JsonResponse({
                "status": "Failed to update !",
            })
    elif request.method == "DELETE":
        todo = Todos.objects.get(id=id)
        todo.delete()
        return JsonResponse({
                "status": "Todo deleted !",
            })

