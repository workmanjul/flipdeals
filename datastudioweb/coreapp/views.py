from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def input(request):
    return render(request, 'input.html', {})

def job_summary(request):
    return render(request, 'job_summary.html', {})

def job_list(request):
    return render(request, 'job_list.html', {})

#TODO remove this, we will use job_list() for client summary list also
def job_list_client(request):
    return render(request, 'job_list_client.html', {})

def client_summary(request):
    return render(request, 'client_summary.html', {})
