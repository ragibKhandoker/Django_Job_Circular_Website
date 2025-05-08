from django.contrib import admin

from .models import JobPost, NetworkingJob, Techjob, UserSignup

# Register your models here.
admin.site.register(Techjob)
admin.site.register(UserSignup)
admin.site.register(NetworkingJob)
admin.site.register(JobPost)