from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
