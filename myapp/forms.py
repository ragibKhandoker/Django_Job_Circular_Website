from django import forms
from django.forms import modelformset_factory

from .models import (Applicant, EducationalBackground,
                     EmployerRegistrationForm, JobApplicationForm, JobPost,
                     UserSignup, WorkExperience)


class SignupForm(forms.ModelForm):
    user_id = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput,required=False)

    class Meta:
        model = UserSignup
        fields = ['fullname', 'email', 'password']

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = [
            'job_id','title','status','requirements','location','salary','educational_level','experience_level','deadline','work_hours',
        ]
        widgets  = {
            'deadline': forms.DateInput(attrs={'type':'date'}),
        }
    def clean(self):
        clean_data = super().clean()
        if not clean_data.get('status'):
            raise forms.ValidationError("Select at least one job")

class EmployerRegistrationModelForm(forms.ModelForm):
    class Meta:
        model = EmployerRegistrationForm
        fields = [
            'Employer_id',
            'company_name',
            'email',
            'phone',
            'password',
            'location',
            'description',
        ]
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'Create a secure password'}),
            'description':forms.Textarea(attrs={'rows':4}),
        }
    def clean_Employer_id(self):
        employer_id = self.cleaned_data.get('Employer_id')
        if employer_id is not None and employer_id < 0:
            raise forms.ValidationError("Id must be positive")
        return employer_id
class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [

            'full_name','email', 'phone', 'address',
            'resume', 'cover_letter','linkedin_profile',
            'portfolio_website'
        ]
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4}),
            'linkedin_profile': forms.URLInput(attrs={'placeholder':'Linkedin Profile URL'}),
            'portfolio_website':forms.URLInput(attrs={'placeholder':'Portfolio Website URL'}),
        }
class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = [
            'company_name',
            'position',
            'responsibilities',
            'start_date',
            'end_date',
            'description',
            'currently_working'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date': forms.DateInput(attrs={'type':'date'}),
            'responsibilities': forms.Textarea(attrs={'rows':4}),
            'description':forms.Textarea(attrs={'rows':4}),
        }

class EducationalBackgroundForm(forms.ModelForm):
    class Meta:
        model = EducationalBackground
        fields = [
            'institution_name', 'degree_type', 'field_of_study',
            'start_year', 'end_year', 'grade',

        ]
        widgets = {
           'start_year':forms.NumberInput(attrs={'min':1900,
                                                 'max':2100,
                                                 'placeholder':'YYYY'}),
           'end_year':forms.NumberInput(attrs={'min':1900,
                                               'max':2100,
                                               'placeholder':'YYYY'}),
           'description':forms.Textarea(attrs={'rows':4}),

        }

WorkExperienceFormSet = modelformset_factory(
    WorkExperience,
    form=WorkExperienceForm,
)
EducationalBackgroundFormSet = modelformset_factory(
    EducationalBackground,
    form=EducationalBackgroundForm,
)
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'full_name', 'email', 'phone', 'address',
            'resume', 'cover_letter','linkedin_profile',
            'portfolio_website'
        ]
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4}),
            'linkedin_profile': forms.URLInput(attrs={'placeholder':'LinkedIn Profile URL'}),
            'portfolio_website':forms.URLInput(attrs={'placeholder':'Portfolio Website URL'}),
        }
