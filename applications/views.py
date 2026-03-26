from django.shortcuts import render

from applications.models import JobApplication
from django.shortcuts import render, redirect  
from .forms import JobForm      
from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login           
from django.contrib.auth.decorators import login_required  

def home(request):
    return render(request, 'applications/home.html')

@login_required
def job_list(request):
    jobs = JobApplication.objects.filter()
    jobs = JobApplication.objects.filter(user=request.user)
    context = {'jobs':jobs}

    return render(request, 'applications/job_list.html',context)

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user 
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
        
    return render(request, 'applications/job_form.html', {'form': form})

@login_required
def edit_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == 'POST':
      
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:

        form = JobForm(instance=job)

    return render(request, 'applications/job_form.html', {'form': form})

@login_required
def delete_job(request, pk):
    job = get_object_or_404(JobApplication, pk=pk, user=request.user)
    
    if request.method == 'POST':
        job.delete() 
        return redirect('job_list')
        
   
    return render(request, 'applications/job_confirm_delete.html', {'job': job})

@login_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/signup.html', {'form': form})