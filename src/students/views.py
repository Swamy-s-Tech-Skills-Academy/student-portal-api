from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student


# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def student_detail_html_view(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student_details.html', {'student': student})
