from django.shortcuts import render

def index(request):
    print("GAD-3")
    return render(request, 'index.html', {'message': 'Hello from AWS Lambda!'})
