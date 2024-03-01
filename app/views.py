from django.shortcuts import render

# Create your views here.
def job_form(request):
    return render(request,'job_form.html')
