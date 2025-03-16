from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import cont
from .forms import contacts
import random
# from django.http import HttpResponse
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def index(request):
    return render(request,'index.html')

#validation register
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.contrib.auth.models import User

def log_reg(request):
    context={}
    if request.method == "POST":
        if request.POST.get('form_type')=='login_form': 
            username = request.POST.get('username')
            password = request.POST.get('password')
        
        # Authenticate user
            user = authenticate(request, username=username,password=password)
            if user is not None:
               login(request, user)  # Log the user in
               return redirect('contact')  # Redirect to the contact page after successful login
            else:
               messages.error(request, 'Incorrect username or password')  # Show error message if authentication fails
            # return render(request, 'log_reg.html')  # Render the login page
            #validate register
        elif request.POST.get('form_type')=='register_form':
             
    
               username = request.POST.get('username')
               email = request.POST.get('email')
               password = request.POST.get('password')
        
        # Check if username already exists
               if not username or not email or not password:
                 messages.error(request,'Please fill all fields')
               elif User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                    context['form_type'] = 'register_form'
                    return render(request, "log_reg.html", {"form_type": "register_form"})  # Example

               else:
            # Create new user and save to database
                  user = User.objects.create_user(username=username, email=email, password=password)
                  user.save()
                  messages.success(request, 'Account successfully created')
                  return redirect('log_reg')
        
        # return redirect("log_reg")  # Redirect to the login page after successful registration
    
    return render(request, 'log_reg.html')  # Render the registration page

#logout validation
def logout_view(request):
    logout(request)
    messages.success(request,'successfully logout')  
    return redirect("log_reg")
 #contact validation

# def contact(request):
#     if request.method=="POST":
#       if request.user.is_authenticated:
 
#          if request.POST.get('form_type')=='contact_form':
#              firstname=request.POST.get('first_name')
#              email=request.POST.get('email')
#              subject=request.POST.get('subject')
#              message=request.POST.get('message')
#              if not firstname or not email or not subject or not message:
#                  messages.error(request,'please fill all the fields') 
#              else:
#                  Ind=contact_for.objects.create(first_name=firstname,email=email,subject=subject,message=message)
#                  Ind.save()
#                  messages.success(request,"Message have been send,Thank you!")
#                  return redirect('contact')

#       else:
#          return redirect('log_reg')

#     return render(request,'contact.html')
# def contact(request):
#     if request.method=="POST":
#         form=contactfor(request.POST)
#         if form.is_valid():
#             form.save()
#             return  redirect('contact')
#     else:
#         form=contactfor()
#     return render(request,'contact.html',{'form':form})
def contact(request):
    if request.method=="POST":
        form = contacts(request.POST)  # Bind the form with POST data
        if form.is_valid():
          form.save()
          return redirect('home')
        else:
            messages.error(request,"error")
    else:
        form=contacts()
    return render(request,'contactt.html',{'form':form})

    
 # Ensure the model is imported correctly


            # Check if any field is empty
           

# Create your views here.
# from .forms import DescriptionForm
# from .forms import AnswerForm
# from .models import interviewprep
# from transformers import pipeline
# question=pipeline("text2text-generation",model="google/flan-t5-large")
# suggested_answer_generator=pipeline("text2text-generation",model="google/flan-t5-large")
# answer_evaluator=pipeline("text-classification",model="distilbert-base-uncased-finetuned-sst-2-english")



# from .forms import job_field
# question_generator=pipeline("text2text-generation",model="google/flan-t5-large")
# sugusted_answer_generator=pipeline("text2text-generation",model="google/flan-t5-large")
# feedback_generator=pipeline("text-classification",model="distilbert-base-uncased-finetuned-sst-2-english")

# def home(request):
#     Description=DescriptionForm()
#     Answer=AnswerForm()
#     job=job_field()
#     practice,feedback=None,None
#     if request.method=="POST":
#         action=request.POST.get('action')
#         if action in ['generate_question','generate_next']:
#             job=job_field(request.POST)
#             Description=DescriptionForm(request.POST)
#             if job.is_valid():
#              domain=job.cleaned_data['job_title']
#              if Description.is_valid():
#               job_description=Description.cleaned_data['description']
#               prompt=f"Generate a technical interview question for a {domain} role. The job involves: {job_description}"
#               question_output=question_generator(prompt,max_length=50,temperature=0.7,top_p=0.9,num_return_sequences=1,do_sample=True)[0]['generated_text']
#               practice=interviewprep.objects.create(description=job_description,question=question_output)
#               practice.save()
#         elif action == "submit_answer":
#             practice_id=request.POST.get('practice_id') 
#             practice=get_object_or_404(interviewprep,id=practice_id) 
#             Answer=AnswerForm(request.POST,instance=practice)  #doubt
#             if Answer.is_valid():
#                 practice.user_ans=Answer.cleaned_data['user_ans']
#                 evaluate_ans=feedback_generator(practice.user_ans)[0]
#                 label,score=evaluate_ans['label'],evaluate_ans['score']

#                 feedback="😀Excellent Answer" if label=="POSITIVE" and score >0.85 else\
#                          "⚠️ Good answer, but you could improve it." if label == "POSITIVE" else \
#                          "❌ Needs improvement."
#                 practice.feedback = feedback
#                 practice.save()
#                 ans_prompt=f"provide a structured answer for he inerview questiion:'{practice.question}' based on {practice.description}."
#                 suggested_answer=sugusted_answer_generator(ans_prompt,max_length=500,num_return_sequences=1,temperature=0.7,top_p=0.9)[0]['generated_text']
#                 practice.suggested_answer=suggested_answer.strip()
#                 practice.save()
#     return render(request,'home.html',{"descriptions":Description,"question":practice.question if practice is not None else "","AnswerForm":AnswerForm,
#                                        "practice_id":practice.id if practice is not None else "",
#                                        "feedback":feedback,
#                                        "sug_ans":practice.suggested_answer if practice is not None else "",
#                                        "job":job}) 
from django import forms
from transformers import pipeline
from .models import interviewprep
from .forms import Job_Details
from .forms import Ans_Form
Question_Generator=pipeline('text2text-generation',model="google/flan-t5-large")
Answer_generator=pipeline('text2text-generation',model="google/flan-t5-large")
Feedback_generator=pipeline('text-classification',model="distilbert-base-uncased-finetuned-sst-2-english")

@login_required
def home(request):
    
    AnswerForm=Ans_Form()
    DetailsForm=Job_Details()
    practice=None
    if request.method=="POST":
        action=request.POST.get('action')
        if action in ['generate_question']: #generate question after the description section
            DetailsForm=Job_Details(request.POST)
            if DetailsForm.is_valid():
                domain=DetailsForm.cleaned_data['domain']
                job_description=DetailsForm.cleaned_data['description']
                request.session['domain']=domain
                request.session['job_description']=job_description
                prompt=f"Generate a technical interview question for a {domain} role. The job involves: {job_description}"
                question_output=Question_Generator(prompt,max_length=50,do_sample=True,temperature=0.7,top_p=0.9,num_return_sequences=1)[0]['generated_text']
                practice=interviewprep.objects.create(user=request.user,domain=domain,description=job_description,question=question_output.strip())
                practice.save()
        elif action=="generate_next":
            domain=request.session.get('domain')
            job_description=request.session.get('job_description')
            prompt=f"Generate a technical interview question for a {domain} role. The job involves: {job_description}"
            question_output=Question_Generator(prompt,max_length=50,top_p=0.9,temperature=0.7,do_sample=50,num_return_sequences=1)[0]['generated_text']
            practice=interviewprep.objects.create(domain=domain,description=job_description,question=question_output.strip())
            practice.save()
        elif action == "submit_answer":#submit for AI feedback answer
                practice_id=request.POST.get('practice_id')
                practice=get_object_or_404(interviewprep,id=practice_id)
                AnswerForm=Ans_Form(request.POST,instance=practice)
                if AnswerForm.is_valid():
                    practice.user_ans=AnswerForm.cleaned_data['user_ans']
                    practice.save()
                    feedback_generated=Feedback_generator(practice.user_ans)[0]
                    label,score=feedback_generated['label'], feedback_generated['score']
                    feedback="😀Excellent Answer, Keep going" if label=="POSITIVE" and score > 0.9 else\
                             "(●'◡'●)Good Answer, but you could improve it" if label=="POSITIVE" and score > 0.75 else\
                             "😐Need improvement."
                    practice.feedback=feedback
                    if not practice.suggested_answer:
                        suggested_ans_proompt=f"provide a structured answer for the interview question:{practice.question} based on {practice.description}."
                        suggested_ans=Answer_generator(suggested_ans_proompt,max_length=500,temperature=0.7,top_p=0.9,top_k=50,num_return_sequences=1)[0]['generated_text']
                        practice.suggested_answer=suggested_ans
                    practice.save()
        elif action=="sug_answer":
                practice_id=request.POST.get('practice_id')
                practice=get_object_or_404(interviewprep,id=practice_id)
                if not practice.suggested_answer:
                    suggested_ans_proompt=f"Provide a structured answer for the interview question: {practice.question} based on {practice.description}."
                    suggested_ans=Answer_generator(suggested_ans_proompt,max_length=500,temperature=0.7,top_p=0.9,top_k=50,num_return_sequences=1)[0]['generated_text']
                    practice.suggested_answer=suggested_ans
                    practice.save()
    return render(request,'home.html',{"practice_id":practice.id if practice is not None else '',
                                       "suggested_ans":practice.suggested_answer if practice is not None else '',
                                       "feedback":practice.feedback if practice is not None else '',
                                       "DetailsForm":DetailsForm,"AnswereForm":AnswerForm,
                                       "question":practice.question if practice is not None else ''}) 

from .models import Job
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
def get_job_description(request):
    domain=request.GET.get('domain')
    if domain:
        try:
           job=Job.objects.get(job_title=domain)
           return JsonResponse({'job_description':job.job_description})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Job description not found for this domain'}, status=404)
    else:
        return JsonResponse({'error': 'No domain provided'}, status=400)
    
from .models import Personality
import json
personality_analysor=pipeline('text-classification',model="google/flan-t5-large")
@login_required
def personality_analysis(request):
    summary_data=interviewprep.objects.filter(user=request.user).values(
        "id", "created_at", "question", "user_ans", "suggested_answer"
    ) 
    summary_list = list(summary_data)

    # Convert datetime fields to strings
    for item in summary_list:
        item["created_at"] = item["created_at"].strftime("%Y-%m-%d %H:%M:%S")  # Convert to string format

    summary_json = json.dumps(summary_list)
    if not summary_data:
        messages.error('request','Sorry,no summary Found!')
        return redirect("personality_analysis")
    answers=interviewprep.objects.filter(user=request.user,user_ans__isnull=False)
    if not answers:
        messages.error(request,'No response available')
        return redirect("personality_analysis")
    traits={
        "openness":50,
        "conscientiousness":50,
        "extraversion":50,
        "agreeableness":50,
        "neuroticism":50
    }
    for response in answers:
        answer=response.user_ans.lower()  #.user_ans because response is an obj but we need string (not sure)
        sentiment=personality_analysor(answer)[0]

        if any(word in answer for word in ["creative","innovative","imaginative","visionary","inventive","artistic"]):
            traits['openness'] += random.randint(5,10)
        if any(word in answer for word in ["organized","structured","methodical","systematic","precise","detail-oriented","thorough"]):
            traits['conscientiousness'] += random.randint(5,10)
        if any(word in answer for word in ["sociable","outgoing","friendly","talkative","gregarious","approachable","carismatic"]):
            traits['extraversion'] += random.randint(5,10)
        if any(word in answer for word in ["kind","caring","compassionate","warm","gentle","generous","nurturing"]):
            traits['agreeableness'] += random.randint(5,10)
        if sentiment['label']=="NEGATIVE":       
            traits["neuroticism"] += random.randint(5,10)
    
    for key in traits:
        traits[key]=max(0,min(traits[key],100))

    personality,object=Personality.objects.update_or_create(
        user=request.user,
        defaults=traits
    )

    return render(request,"summary.html",{"traits":json.dumps(traits), "summary":summary_json})

