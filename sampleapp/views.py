from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# from .models import cont
from .forms import contacts
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
from .forms import DescriptionForm
from .forms import AnswerForm
from .models import interviewprep
from transformers import pipeline
# question=pipeline("text2text-generation",model="google/flan-t5-large")
# suggested_answer_generator=pipeline("text2text-generation",model="google/flan-t5-large")
# answer_evaluator=pipeline("text-classification",model="distilbert-base-uncased-finetuned-sst-2-english")
# def home(request):
#     descriptions=DescriptionForm()
    # answere=AnswerForm()
    # practice, feedback, suggested_answer=None, None, None
    # if request.method =="POST":
    #     action=request.POST.get('action')
    #     if action in['generate_question']:
    #         descriptions=DescriptionForm(request.POST)
    #         descriptions.is_valid()
    #         descriptions.save()
    #     else:
    #         messages.error(request,"an error")
    # return render(request,'home.html',{"descriptions":descriptions})
    #         if descriptions.is_valid():
    #             job_description=descriptions.cleaned_data['description']
    #             prompt = f"Generate a technical interview question for the job description:{job_description}."
    #             question_output=question(prompt,max_length=50,num_return_sequences=1,do_sample=True,temperature=0.7,top_p=0.9)[0]['generated_text']
    #             practice=interviewprep.objects.create(description=job_description, question=question_output.strip())
                
    #     elif action=="submit_answer":
    #         answere=AnswerForm(request.POST, instance=practice)
    #         if answere.is_valid():
    #             practice.user_ans=answere.cleaned_data(practice.user_ans)
    #             evaluation_result = answer_evaluator(practice.user_answer)[0]
    #             label, score = evaluation_result['label'], evaluation_result['score']

    #             feedback = "✅ Excellent response!" if label == "POSITIVE" and score > 0.85 else \
    #                        "⚠️ Good answer, but you could improve it." if label == "POSITIVE" else \
    #                        "❌ Needs improvement."

    #             practice.feedback = feedback
    #             practice.save()
                
    #     elif action == "get_suggested_answer":
    #         answer_prompt = f"Provide a structured answer for the interview question: '{practice.question}' based on {practice.job_description}."
    #         suggested_answer_output = suggested_answer_generator(
    #             answer_prompt, max_length=500, num_return_sequences=1, do_sample=True, temperature=0.7, top_p=0.9
    #         )[0]['generated_text']

    #         practice.suggested_answer = suggested_answer_output.strip()
    #         practice.save()
    #         suggested_answer = practice.suggested_answer


    # return render(request,'home.html',{"descriptions":descriptions})
# ,"answere":answere, "question":interviewprep.question if practice else None
from .forms import job_field
question_generator=pipeline("text2text-generation",model="google/flan-t5-large")
sugusted_answer_generator=pipeline("text2text-generation",model="google/flan-t5-large")
feedback_generator=pipeline("text-classification",model="distilbert-base-uncased-finetuned-sst-2-english")

def home(request):
    Description=DescriptionForm()
    Answer=AnswerForm()
    job=job_field()
    practice,feedback=None,None
    if request.method=="POST":
        action=request.POST.get('action')
        if action in ['generate_question','generate_next']:
            job=job_field(request.POST)
            Description=DescriptionForm(request.POST)
            if job.is_valid():
             domain=job.cleaned_data['job_title']
             if Description.is_valid():
              job_description=Description.cleaned_data['description']
              prompt=f"Generate a technical interview question for a {domain} role. The job involves: {job_description}"
              question_output=question_generator(prompt,max_length=50,temperature=0.7,top_p=0.9,num_return_sequences=1,do_sample=True)[0]['generated_text']
              practice=interviewprep.objects.create(description=job_description,question=question_output)
              practice.save()
        elif action == "submit_answer":
            practice_id=request.POST.get('practice_id') 
            practice=get_object_or_404(interviewprep,id=practice_id) 
            Answer=AnswerForm(request.POST,instance=practice)  #doubt
            if Answer.is_valid():
                practice.user_ans=Answer.cleaned_data['user_ans']
                evaluate_ans=feedback_generator(practice.user_ans)[0]
                label,score=evaluate_ans['label'],evaluate_ans['score']

                feedback="😀Excellent Answer" if label=="POSITIVE" and score >0.85 else\
                         "⚠️ Good answer, but you could improve it." if label == "POSITIVE" else \
                         "❌ Needs improvement."
                practice.feedback = feedback
                practice.save()
                ans_prompt=f"provide a structured answer for he inerview questiion:'{practice.question}' based on {practice.description}."
                suggested_answer=sugusted_answer_generator(ans_prompt,max_length=500,num_return_sequences=1,temperature=0.7,top_p=0.9)[0]['generated_text']
                practice.suggested_answer=suggested_answer.strip()
                practice.save()
    return render(request,'home.html',{"descriptions":Description,"question":practice.question if practice is not None else "","AnswerForm":AnswerForm,
                                       "practice_id":practice.id if practice is not None else "",
                                       "feedback":feedback,
                                       "sug_ans":practice.suggested_answer if practice is not None else "",
                                       "job":job}) 