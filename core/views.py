from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital
def TextResponse(string):
    return HttpResponse(string.encode('utf-8'),content_type='text/plain; charset=utf8')
# Create your views here.

def greet(request):
    data = request.GET
    data = {'hospital_number':"9944941964"}#Mock
    # validation

    hospital = Hospital.objects.get(number=data['hospital_number'])
    if hospital.greeting:
        return TextResponse(hospital.greeting)
    else:
        greeting = "Welcome to {}. To reserve your spot in the queue, press 1.".format(hospital.name)
        return TextResponse(greeting)
