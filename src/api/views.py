from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.


def students_view(request):
    students = list(Student.objects.values())

    return JsonResponse(students, safe=False)
