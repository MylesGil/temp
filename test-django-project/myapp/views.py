from django.shortcuts import render

def index(request):
    print("GAD-11")
    return render(request, 'index.html', {'message': 'Hello from AWS Lambda!'})
