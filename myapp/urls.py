from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .views import (candidate_login_view, candidate_signup_view,
                    choose_role_view, employee_login_view,
                    employee_signup_view, home_view, login_choice_view,
                    logout_view)

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.home_view, name='home'),
    # path('login/', views.login_view, name='login'),
    path('signup/', views.choose_role_view, name='signup'),
    path('signup/employee/', views.employee_signup_view, name='employee_signup'),
    # path('signup/employee/', employee_signup_view, name='employee_signup'),
    path('signup/candidate/', candidate_signup_view, name='candidate_signup'),
    path('apply/<int:job_id>/', views.apply_form, name='apply_form'),
    path('jobs/category/<str:category>/', views.job_category_view, name='job_category'),
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('job-list/', views.job_list, name='job_list'),
    path('jobs/total/', views.total_jobs_view, name='TotalJob'),
    path('application-success/', views.application_success, name='application_success'),
    path('apply-success/', views.apply_success, name='apply_success'),
    path('browse-candidates/',views.browse_candidates,name='browse_candidates'),
    path('candidate/<int:applicant_id>/',views.candidate_detail,name="candidate_detail"),
    # path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('login/',views.login_choice_view,name='login'),
    path('login/employee/',views.employee_login_view,name='employee_login'),
    path('login/candidate/',views.candidate_login_view,name='candidate_login'),
    path('logout/',logout_view,name='logout')
]
