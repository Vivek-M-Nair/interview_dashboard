from django.db import models
from django.contrib.auth.models import User
class contact_for(models.Model):
    first_name=models.TextField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=600)
    def __str__(self):
        return self.first_name
class cont(models.Model):
    firstname=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
    def __str__(self):
        return self.si

class Job(models.Model):
    job_title=models.CharField(max_length=50)
    job_description=models.TextField()

    def __str__(self):
        return self.job_title

class interviewprep(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    domain=models.CharField(max_length=50)
    description=models.TextField()
    user_ans=models.TextField()
    question=models.TextField()
    suggested_answer=models.TextField()
    feedback=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Personality(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    openness=models.IntegerField()
    conscientiousness=models.IntegerField()
    extraversion=models.IntegerField()
    agreeableness=models.IntegerField()
    neuroticism=models.IntegerField()