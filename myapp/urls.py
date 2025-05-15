from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .views import (candidate_signup_view, choose_role_view,
                    employee_signup_view, home_view, login_view)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.choose_role_view, name='signup'),
   #  path('register/', views.login_view,name='register'),
    path('signup/employee/', views.employee_signup_view, name='employee_signup'),

    path('signup/employee/', employee_signup_view, name='employee_signup'),
    path('signup/candidate/', candidate_signup_view, name='candidate_signup'),
    path('apply/<int:job_id>/', views.apply_form, name='apply_form'),
    # path('apply/<int:job_id>/', views.apply_job_view, name='apply_job'),

    path('jobs/category/<str:category>/', views.job_category_view, name='job_category'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('job-list/', views.job_list, name='job_list'),
    path('jobs/total/', views.total_jobs_view, name='TotalJob'),
    path('application-success/', views.application_success, name='application_success'),
    path('apply-success/', views.apply_success, name='apply_success'),
    #  path('candidate/signup/', views.candidate_signup, name='candidate_signup'),

   # path('apply/success/', views.apply_success, name='apply_success'),



]
