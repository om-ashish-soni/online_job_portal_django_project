from django.db import models
from datetime import datetime

class User(models.Model):

    email=models.CharField(max_length=100)
    isHr=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email + self.isHr

class Application(models.Model):
    appid = models.AutoField(primary_key=True)
    hremail=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    jobfunction=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    salary=models.CharField(max_length=100)

class Applicant(models.Model):
    applicantid=models.AutoField(primary_key=True)
    candidateemail=models.CharField(max_length=100)
    appid=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    birthdate=models.CharField(max_length=100)
    expected_salary=models.CharField(max_length=100)
    resume_url=models.CharField(max_length=1000)
    progress=models.CharField(max_length=100)
    pass