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

class Job_Details(forms.ModelForm):
    Job_Field=[("software Engineering","Software Engineering"),
               ("Data Science","Data Science")]
    domain=forms.ChoiceField(choices=Job_Field)
    
    class Meta:
        model=interviewprep
        fields=['domain','description']

class Ans_Form(forms.ModelForm):
    class Meta:
        model=interviewprep
        fields=['user_ans']
    