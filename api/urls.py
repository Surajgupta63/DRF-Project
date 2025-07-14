from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('students/', views.studentsView, name='studentsView'),
    path('students/<int:pk>/', views.studentDetailView, name='studentDetailView'),

    ## ClassBased View
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetails.as_view()),

    ## ViewSet view
    path('', include(router.urls))
]