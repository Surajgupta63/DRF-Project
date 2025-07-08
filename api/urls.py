from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView, name='studentsView'),
    path('students/<int:pk>/', views.studentDetailView, name='studentDetailView'),
    path('employees/', views.Employees.as_view()),
]