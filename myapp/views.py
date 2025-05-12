import re

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import (ApplicantForm, EducationalBackgroundFormSet,
                    EmployerRegistrationForm, JobApplicationForm, JobPostForm,
                    SignupForm, WorkExperienceForm, WorkExperienceFormSet)
from .models import (EducationalBackground, JobApplicationForm, JobPost,
                     NetworkingJob, Techjob, UserSignup, WorkExperience)

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

# def delete_job(request,job_id):
#     job = get_object_or_404(JobPost, id=job_id)
#     if request.method == 'POST':
#         job.delete()
#         messages.success(request,'Job deleted successfully!')
#         return redirect('job_list')
#     return render(request,'jobs/confirm_delete.html',{'jobs':job})
def delete_job(request, job_id):
    # Delete the job and related applications
    JobPost.objects.filter(id=job_id).delete()
    return redirect('job_list')

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

# def apply_form(request,job_id):
#     job = get_object_or_404(JobPost,id = job_id)
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         cover_letter = request.POST.get('cover_letter')
#         resume = request.FILES.get('resume')
#         ApplicationForm.objects.create(
#             job=job,
#             full_name = full_name,
#             email=email,
#             phone = phone,
#             cover_letter = cover_letter,
#             resume = resume

#         )
#         messages.success(request,'Application submitted successfully!')
#         return redirect('application_success')
#     return render(request,'apply_form.html',{'jobs':job})









# def apply_form(request, job_id):
#     job = get_object_or_404(JobPost, id=job_id)

#     if request.method == 'POST':
#         applicant_form = ApplicantForm(request.POST, request.FILES)
#         work_formset = WorkExperienceFormSet(request.POST, prefix='work')
#         edu_formset = EducationalBackgroundFormSet(request.POST, prefix='edu')

#         if applicant_form.is_valid() and work_formset.is_valid() and edu_formset.is_valid():
#             applicant = applicant_form.save(commit=False)
#             applicant.job = job
#             applicant.save()

#             work_formset.instance = applicant
#             work_formset.save()

#             edu_formset.instance = applicant
#             edu_formset.save()

#             return redirect('apply_success')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         applicant_form = ApplicantForm()
#         work_formset = WorkExperienceFormSet(prefix='work')
#         edu_formset = EducationalBackgroundFormSet(prefix='edu')

#     return render(request, 'apply_form.html', {
#         'job': job,
#         'form': applicant_form,
#         'work_formset': work_formset,
#         'edu_formset': edu_formset
#     })

def apply_form(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)

    if request.method == 'POST':
        applicant_form = ApplicantForm(request.POST, request.FILES)
        work_formset = WorkExperienceFormSet(request.POST, prefix='work')
        edu_formset = EducationalBackgroundFormSet(request.POST, prefix='edu')

        if applicant_form.is_valid() and work_formset.is_valid() and edu_formset.is_valid():
            applicant = applicant_form.save(commit=False)
            applicant.job = job
            applicant.save()
            applicant.work_experiences.all()
            applicant.educational_backgrounds.all()


            # applicant.workexperience_set.all().delete()
            # applicant.educationalbackground_set.all().delete()

            for work_exp in work_formset.save(commit=False):
                work_exp.applicant = applicant
                work_exp.save()

            for edu in edu_formset.save(commit=False):
                edu.applicant = applicant
                edu.save()
            # return redirect('apply_success')
            # return render(request, 'application_submitted.html', {'applicant': applicant})
            return render(request, 'application_submitted.html', {
    'applicant': applicant,
    'work_experiences': applicant.work_experiences.all(),
    'educational_backgrounds': applicant.educational_backgrounds.all()
})



        else:
            print(applicant_form.errors)
            print(work_formset.errors)
            print(edu_formset.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        applicant_form = ApplicantForm()
        work_formset = WorkExperienceFormSet(prefix='work')
        edu_formset = EducationalBackgroundFormSet(prefix='edu')
    return render(request, 'apply_form.html', {
        'job': job,
        'form': applicant_form,
        'work_formset': work_formset,
        'edu_formset': edu_formset
    })







def apply_job(request,job_id):
    job = JobPost.objects.get(id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.job = job
            applicant.save()
            return redirect('success_page')
    else:
        form = ApplicationForm()
    return render(request,'apply_form.html',{'application_form':form,'job':job})
def save_personal_info(request):
    if request.method == 'POST':
        applicant = Applicant(
            full_name = request.POST.get('full_name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            address = request.POST.get('address'),
            cover_letter = request.POST.get('cover_letter'),
            resume = request.FILES.get('resume'),
            linkedIn_profile = request.POST.get('linkedIn_profile'),
            portfolio_website = request.POST.get('portfolio_website')
        )
        applicant.save()
        return redirect('application_success')
    return render(request,'apply_form.html')
def application_view(request):
    if request.method == 'POST':
        print("Form submitted")
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = ApplicationForm()
    return render(request,'application.html',{'form':form})
def application_success(request):
    return render(request,'application_success.html')

def apply_success(request):
    return render(request, 'apply_success.html')