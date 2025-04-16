from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def students_list(request):
    # create a list of students
    students = [
        {"name": "John Doe", "age": 20},
        {"name": "Jane Smith", "age": 22},
        {"name": "Alice Johnson", "age": 19},
    ]
    return HttpResponse(students)
