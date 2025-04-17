from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def students_view(request):
    if request.method == 'GET':
        # retrieve all students from the Student table
        students = Student.objects.all()
        # serialize the data using the StudentSerializer
        serializer = StudentSerializer(students, many=True)
        # return the serialized data as JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)


def students_view_manual(request):
    students = Student.objects.all()
    print(students)

    # Manually convert the queryset to a list of dictionaries for JSON serialization
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
