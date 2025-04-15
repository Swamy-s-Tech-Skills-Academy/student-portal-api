from django.shortcuts import render


# Create your views here.
def students_view(request):

    return render(request, 'students.html')
