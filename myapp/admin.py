from django.contrib import admin

from .models import JobPost, NetworkingJob, Techjob, UserSignup

# @admin.register(Applicant)
# class ApplicantAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'phone', 'address', 'resume', 'cover_letter', 'linkedIn_profile', 'portfolio_website')
#     search_fields = ('full_name', 'email')
#     list_filter = ('created_at',)
#     ordering = ('-created_at',)
# Register your models here.
admin.site.register(Techjob)
admin.site.register(UserSignup)
admin.site.register(NetworkingJob)
admin.site.register(JobPost)