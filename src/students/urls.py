from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('<str:student_id>/', views.student_detail_html_view, name='student_detail_html_view'),
]