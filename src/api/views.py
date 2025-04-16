from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.


def students_view(request):
    students = Student.objects.all()
    print(students)

    # Manually convert the queryset to a list of dictionaries for JSON serialization
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
