from django.urls import path

from . import views
from .views import (choose_role_view, employee_signup_view, home_view,
                    login_view, signup_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/',choose_role_view,name = 'signup'),
    path('signup/employee/',employee_signup_view,name ='employee_signup'),
    path('signup/candidate/',signup_view,name = 'candidate_signup'),
    path('apply/<int:job_id>/',views.tech_apply,name='apply'),
    path('apply/<int:job_id>/',views.apply_job_view,name='apply_job'),
    path('jobs/category/<str:category>/',views.job_category_view,name = 'job_category'),
    path('delete_job/<int:job_id>/',views.delete_job,name = 'delete_job'),
    path('post-job/',views.post_job,name='post_job'),
    path('job-list/',views.job_list,name = 'job_list'),
    path('jobs/total/', views.total_jobs_view, name='TotalJob'),
]
