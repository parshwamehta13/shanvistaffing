from __future__ import unicode_literals

from django.db import models
import datetime
from time import time
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

# Model for Job Opening
class JobOpening (models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    min_salary = models.PositiveIntegerField()
    max_salary = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    min_requirement = models.TextField()
    job_description = models.TextField()
    posting_date = models.DateField(default=datetime.date.today)
    about_company = models.TextField()

    def __str__ (self):
        return self.position+" "+self.company_name

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Candidate (models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    current_designation = models.CharField(max_length=100)
    current_employer = models.CharField(max_length=100)
    current_ctc = models.PositiveIntegerField()
    expected_ctc = models.PositiveIntegerField()
    notice_period = models.PositiveIntegerField()
    total_exp_yrs = models.PositiveIntegerField()
    total_exp_mts = models.PositiveIntegerField()
    highest_qual = models.CharField(max_length=100)
    college_highest_qual = models.CharField(max_length=100)
    current_location = models.CharField(max_length=100)
    cv = models.FileField(upload_to=get_upload_file_name)

    def __str__ (self):
        return self.name

class JobApplication(models.Model):
    candidate = models.ForeignKey(User)
    position = models.ForeignKey(JobOpening)
    application_date = models.DateField(default=datetime.date.today)
    status_choice = (('Pending','Pending'),('Shortlisted','Shortlisted'))
    status = models.CharField(choices=status_choice,max_length=20,default='Pending')
    comment = models.TextField(blank=True)

    def __str__ (self):
        return self.candidate.username + " - " + self.position.position + " - " + self.position.company_name

class Requirement (models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    cont_no=models.CharField(max_length=20)
    job_description=models.TextField()
    further_info=models.FileField(upload_to=get_upload_file_name)

    def __str__ (self):
        return self.full_name + " - " + self.company_name