from django import forms
# from .models import interviewprep
from .models import contact_for

class contactfor(forms.ModelForm):
     class Meta:
         model = contact_for  # Ensure the model is linked here
         fields = ['first_name', 'email', 'subject', 'message']  # Specify the fields
    
from django import forms
from .models import cont
# from .models import interviewprep
# from .models import Job
class contacts(forms.ModelForm):
    class Meta:
        model=cont
        fields=['firstname','email','subject','message']

# class DescriptionForm(forms.ModelForm):
#     class Meta:
#         model=interviewprep
#         fields=['description']
# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model=interviewprep
#         fields=['user_ans']
# from django import forms
# from .models import Job  # Ensure Job model is correctly imported

# class job_field(forms.ModelForm):  # Keeping class name as requested
#     JOB_TITLES = [
#         ("Software Engineer", "Software Engineer"),  # Fixed label
#         ("Data Scientist", "Data Scientist")
#     ]
    
#     job_title = forms.ChoiceField(choices=JOB_TITLES)

#     class Meta:
#         model = Job  # Ensure 'Job' model exists
#         fields = ['job_title']
from .models import interviewprep
from .models import Job

class Job_Details(forms.ModelForm):
    # Job_Field=[("software Engineering","Software Engineering"),
    #            ("Data Science","Data Science")]
    domain=forms.ChoiceField(
        choices=[(job.job_title,job.job_title) for job in Job.objects.all()],
        widget=forms.Select(attrs={'class':'domain'}),
    )
    
    class Meta:
        model=interviewprep
        fields=['domain','description']
        widgets={
                 'description':forms.Textarea(attrs={'class':'job_description', 'placeholder':'Your Job Description'})
                 }
  #forms.TextInput - Charfeild
class Ans_Form(forms.ModelForm):
    class Meta:
        model=interviewprep
        fields=['user_ans']


# from django import forms
# from .models import Job, Job_Details

# class JobDetailsForm(forms.ModelForm):
#     domain = forms.ChoiceField(choices=[])

#     class Meta:
#         model = Job_Details
#         fields = ['domain', 'job_description']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Get the job titles from the Job model
#         job_titles = Job.objects.values_list('job_title', 'job_title')

#         # Set the choices dynamically for the domain field
#         self.fields['domain'].choices = [(title, title) for title in job_titles]
