from django.shortcuts import render, HttpResponse

# Create your views here.
def students(request):
    student = [{
        'id': 1,
        'name': 'Suraj Gupta',
        'age': 21
    }]

    return HttpResponse(student)