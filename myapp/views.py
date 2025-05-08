import re

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import (ApplicationForm, EducationalBackgroundFormSet,
                    EmployerRegistrationForm, JobApplicationForm, JobPostForm,
                    SignupForm, WorkExperienceFormSet, WorkExperinceFormset)
from .models import (JobApplicationForm, JobPost, NetworkingJob, Techjob,
                     UserSignup)

email_address=''
password=''
confirm_password=''
# Create your views here.
def home_view(request):
    latest_jobs = JobPost.objects.order_by('-created_at')[:4]
    return render(request,'home.html',{'latest_jobs':latest_jobs})

def login_view(request):
    return render(request, 'login.html')

def total_jobs_view(request):
    location = request.GET.get('location','')
    latest = request.GET.get('latest')
    if location:
        jobs = JobPost.objects.filter(location_icontains=location).order_by('-id')
        if latest:
            jobs = jobs[:10]
    else:
        jobs = JobPost.objects.all().order_by('-id')
    return render(request,'total_jobs.html',{'jobs':jobs})

def choose_role_view(request):
    return render(request,'registration_choose.html')

def employee_signup_view(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmployerRegistrationForm()
    return render(request,'employer_registration.html',{'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully!")
            return redirect('login')
        else:
            messages.error(request,"Please fix the errors first")
    else:
        form = SignupForm()

    return render(request,'signup.html',{'form':form})

def job_category_view(request, category):
    jobs = JobPost.objects.filter(title=category)
    context = {
        'jobs':jobs,
        'is_category_page': True
    }
    return render(request,'job_list.html',context)

def technology_jobs_view(request):
    jobs = JobPost.objects.filter(title="Technology")
    return render(request,'technology_jobs.html',{'jobs':jobs})

def networking_jobs_view(request):
    jobs = JobPost.objects.filter(title="Networking")
    return render(request,'networking_jobs.html',{'jobs':jobs})

def engineering_jobs_view(request):
    jobs = JobPost.objects.filter(title='Engineering')
    return render(request,'engineering_jobs.html',{'jobs':jobs})

def marketing_jobs_view(request):
    jobs = JobPost.objects.filter(title='Marketing')
    return render(request,'marketing_jobs.html',{'jobs':jobs})

def content_jobs_view(request):
    jobs = JobPost.objects.filter(title='Content Writing')
    return render(request,'content_jobs.html',{'jobs':jobs})

def customer_support_view(request):
    jobs = JobPost.objects.filter(title='Customer Support')
    return render(request,'customer_jobs.html',{'jobs':jobs})

def finance_jobs_view(request):
    jobs = JobPost.objects.filter(title='Finance')
    return render(request,'finance_jobs.html',{'jobs':jobs})

def health_jobs_view(request):
    jobs = JobPost.objects.filter(title='Healthcare')
    return render(request,'health_jobs.html',{'jobs':jobs})

def design_jobs_view(request):
    jobs = JobPost.objects.filter(title='Design')
    return render(request,'design_jobs.html',{'jobs':jobs})

def education_jobs_view(request):
    jobs = JobPost.objects.filter(title='Education')
    return render(request,'education_jobs.html',{'jobs':jobs})

def tech_apply(request,job_id):
    try:
        job = Techjob.objects.get(pk=job_id)
    except Techjob.DoesNotExist:
        return HttpResponse("Job not found",status=404)
    return render(request,'apply.html',{'job':job})
def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/job-list/?posted=true')
    else:
        form = JobPostForm()

    return render(request,'post_job.html',{'form':form})

def create_job(request):
    form = JobPostForm()
    return render(request,'post_job.html',{'form':form})

def job_list(request):
    jobs = JobPost.objects.all()
    context = {
        'jobs':jobs,
        'is_category_page':False
    }
    return render(request,'job_list.html',context)

def delete_job(request,job_id):
    job = get_object_or_404(JobPost, id=job_id)
    if request.method == 'POST':
        job.delete()
        messages.success(request,'Job deleted successfully!')
        return redirect('job_list')
    return render(request,'jobs/confirm_delete.html',{'jobs':job})
def apply_view(request,job_id):
    job = get_object_or_404(JobPost,id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('apply_success')
    else:
        form = JobApplicationForm()
    return render(request,'apply.html',{'jobs':job,'form':form})



def apply_job_view(request,job_id):
    job = get_object_or_404(JobPost,id = job_id)
    return render(request,'apply_success.html',{'job':job})

def apply_form(request,job_id):
    job = get_object_or_404(JobPost,id = job_id)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')
        ApplicationForm.objects.create(
            job=job,
            full_name = full_name,
            email=email,
            phone = phone,
            cover_letter = cover_letter,
            resume = resume

        )
        messages.success(request,'Application submitted successfully!')
        return redirect('application_success')
    return render(request,'apply_form.html',{'jobs':job})

def application_success(request):
    return render(request,'application_success.html')

def apply_job(request):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST,request.FILES)
        work_experience_formset = WorkExperienceFormSet(request.POST,prefix='work')
        education_formset = EducationalBackgroundFormSet(request.POST,prefix='edu')
        if application_form.is_valid() and work_experience_formset.is_valid() and education_formset.is_valid():
            applicant = application_form.save()
            for form in work_experience_formset:
                instance = form.save(commit=False)
                if form.cleaned_data and not form.cleaned_data.get('DELETE',False):
                    instance.applicant = applicant
                    instance.save()
