from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.


def students_view(request):
    students = Student.objects.all()
    print(students)

    return JsonResponse(list(students.values()), safe=False)
