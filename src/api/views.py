from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def students_view(request):
    students = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 23}
    ]
    
    return JsonResponse(students, safe=False)
