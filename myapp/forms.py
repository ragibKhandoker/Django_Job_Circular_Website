from django import forms

from .models import (EmployerRegistrationForm, JobApplicationForm, JobPost,
                     UserSignup)


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
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplicationForm
        fields = ['name','email','resume']
