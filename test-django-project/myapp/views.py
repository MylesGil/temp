from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'message': 'Hello from AWS Lambda!'})
