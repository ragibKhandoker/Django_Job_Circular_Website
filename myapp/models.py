from django import forms
from django.db import models
from django.utils import timezone


class UserSignup(models.Model):
    fullname = models.CharField(max_length=100,null="True")
    email = models.EmailField(null="True")
    password = models.CharField(max_length=100,null="True")
    confirm_password = models.CharField(max_length=100,null="True")

class ApplicantSignupForm(forms.Form):
    applicant_id = models.CharField(default=0)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname

class EmployerRegistrationForm(models.Model):
    Employer_id = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Techjob(models.Model):
    title = models.CharField(max_length=100,blank=True)
    requirements = models.CharField(max_length =100, blank=True)
    responsibilities = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title

class NetworkingJob(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    requirements = models.TextField(max_length=10000)
    responsibilities = models.TextField(max_length=10000)
    location = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# class JobPost(models.Model):
    # JOB_CHOICES = [
    #     ("Technology", "Technology"),
    #     ("Networking", "Networking"),
    #     ("Engineering", "Engineering"),
    #     ("Marketing", "Marketing"),
    #     ("Content Writing", "Content Writing"),
    #     ("Customer Support", "Customer Support"),
    #     ("Finance", "Finance"),
    #     ("Healthcare", "Healthcare"),
    #     ("Design", "Design"),
    #     ("Education", "Education"),
    # ]
    # job_id = models.IntegerField(default=0)
    # title = models.CharField(max_length=200, choices= JOB_CHOICES)
    # location = models.CharField(max_length=100)
    # # created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # SALARY_CHOICES = [
    #     ('<20000', 'Less than 20,000'),
    #     ('20000-40000', '20,000 - 40,000'),
    #     ('40000-60000', '40,000 - 60,000'),
    #     ('60000-80000', '60,000 - 80,000'),
    #     ('80000-100000', '80,000 - 100,000'),
    #     ('>100000', 'More than 100,000'),
    # ]
    # salary = models.CharField(max_length=100,choices= SALARY_CHOICES)
    # STATUS_CHOICES = [
    #     ("full_time", "Full time"),
    #     ("part_time", "Part time"),
    #     ("remote", "Remote"),
    #     ("hibrid", "Hibrid"),
    #     ("internship", "Internship"),
    #     ("contractual", "Contractual"),
    # ]

    # HOURS_CHOICES = [
    #     (1, '1-10 hours'),
    #     (2, '11-20 hours'),
    #     (3, '21-30 hours'),
    #     (4, '31-40 hours'),
    #     (5, '40+ hours'),
    # ]
    # work_hours = models.IntegerField(choices=HOURS_CHOICES)
    # status = models.CharField(choices=STATUS_CHOICES,max_length=100)
    # requirements = models.TextField(max_length=400)
    # EDUCATION_CHOICES = [
    #     ('high_school', 'High School'),
    #     ('bachelors', "Bachelor's"),
    #     ('masters', "Master's"),
    #     ('phd', 'PhD'),
    # ]
    # educational_level = models.CharField(max_length=20,choices= EDUCATION_CHOICES)

    # EXPERIENCE_CHOICES = [
    #     ('entry_level', 'Entry Level (0-2 years)'),
    #     ('mid_level', 'Mid Level (3-5 years)'),
    #     ('senior_level', 'Senior Level (5+ years)'),
    # ]
    # created_at = models.DateTimeField(auto_now_add= True)
    # experience_level = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)

    # deadline = models.DateField(null=True,blank=True)

    # def __str__(self):
    #     return f"{self.title} ({self.status})"
class JobPost(models.Model):
    JOB_CHOICES = [
        ("Technology", "Technology"),
        ("Networking", "Networking"),
        ("Engineering", "Engineering"),
        ("Marketing", "Marketing"),
        ("Content Writing", "Content Writing"),
        ("Customer Support", "Customer Support"),
        ("Finance", "Finance"),
        ("Healthcare", "Healthcare"),
        ("Design", "Design"),
        ("Education", "Education"),
    ]

    SALARY_CHOICES = [
        ('<20000', 'Less than 20,000'),
        ('20000-40000', '20,000 - 40,000'),
        ('40000-60000', '40,000 - 60,000'),
        ('60000-80000', '60,000 - 80,000'),
        ('80000-100000', '80,000 - 100,000'),
        ('>100000', 'More than 100,000'),
    ]

    STATUS_CHOICES = [
        ("full_time", "Full time"),
        ("part_time", "Part time"),
        ("remote", "Remote"),
        ("hibrid", "Hibrid"),
        ("internship", "Internship"),
        ("contractual", "Contractual"),
    ]

    HOURS_CHOICES = [
        (1, '1-10 hours'),
        (2, '11-20 hours'),
        (3, '21-30 hours'),
        (4, '31-40 hours'),
        (5, '40+ hours'),
    ]

    EDUCATION_CHOICES = [
        ('high_school', 'High School'),
        ('bachelors', "Bachelor's"),
        ('masters', "Master's"),
        ('phd', 'PhD'),
    ]

    EXPERIENCE_CHOICES = [
        ('entry_level', 'Entry Level (0-2 years)'),
        ('mid_level', 'Mid Level (3-5 years)'),
        ('senior_level', 'Senior Level (5+ years)'),
    ]

    job_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200, choices=JOB_CHOICES)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=100, choices=SALARY_CHOICES)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    work_hours = models.IntegerField(choices=HOURS_CHOICES)
    requirements = models.TextField(max_length=400)
    educational_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.status})"

class JobApplicationForm(models.Model):
    job = models.ForeignKey(JobPost,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resume/')
    applied_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Application by {self.name} for {self.job.title}"
