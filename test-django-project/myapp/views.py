from django.shortcuts import render

def index(request):
    print("GAD-5")
    return render(request, 'index.html', {'message': 'Hello from AWS Lambda!'})
