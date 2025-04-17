from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_view, name='students_view'),
    path('students/<int:student_id>/', views.student_detail_view, name='student_detail_view'),
    path('studentsmanual/', views.students_view_manual,
         name='students_view_manual'),
]
