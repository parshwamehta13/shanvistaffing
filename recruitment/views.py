from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required	
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib import messages
# Create your views here.

def index (request):
	if request.user.is_authenticated():
		login_var=True
	else:
		login_var=False
	return render (request,'recruitment/index.html',{'title':'Shanvi Staffing | Get The Job You Deserve !','login':login_var,'username':request.user.username})

def joblist (request):
	if request.user.is_authenticated():
		login_var=True
	else:
		login_var=False
	if 'location' in request.GET and 'role' in request.GET:
		print 'Location '+request.GET['location']+' Searched'
		job_list = JobOpening.objects.filter(location__icontains=request.GET['location']) & JobOpening.objects.filter(position__icontains=request.GET['role'])
	else:
		job_list = JobOpening.objects.all()
	return render (request,'recruitment/joblist.html',{'title':'Shanvi Staffing | List Of Job Openings','job_list':job_list,'login':login_var,'username':request.user.username})

def jobpage (request,job_id):
	if request.user.is_authenticated():
		login_var=True
	else:
		login_var=False
	job = JobOpening.objects.get(pk=job_id)
	title = job.position+" - "+job.company_name
	return render (request,'recruitment/jobpage.html',{'title':'Shanvi Staffing | '+title,'job':job,'login':login_var,'username':request.user.username,'job_id':job_id})

def login_view (request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
		    if user.is_active:
		    	login (request,user)
		        print("User is valid, active and authenticated")
		        messages.success(request, 'Logged In Successfully')
		        return redirect('index')
		    else:
		        print("The password is valid, but the account has been disabled!")
		else:
		    print("The username and password were incorrect.")
		    # Add Message Here
	return render (request,'recruitment/login.html',{'title':'Shanvi Staffing | User Login'})

def update_information(request):	
	candidate = Candidate.objects.get(user=request.user)
	user = request.user
	if request.method == 'POST':
		name=request.POST['full_name']
		email=request.POST['email']
		phone_number=request.POST['mobile_no']
		current_designation=request.POST['current_designation']
		current_employer=request.POST['current_employer']
		current_ctc=request.POST['current_salary']
		expected_ctc=request.POST['expected_salary']
		notice_period=request.POST['notice_period']
		total_exp_yrs=request.POST['total_exp_yrs']
		total_exp_mts=request.POST['total_exp_mts']
		highest_qual=request.POST['highest_qual']
		college_highest_qual=request.POST['college_highest_qual']
		current_location=request.POST['current_location']
		if 'cv' in request.FILES and request.FILES['cv']:
			cv=request.FILES['cv']
		password = request.POST['password']
		if  authenticate(username=request.user.username,password=password):
			print "Update Profile"
			candidate.name = name
			candidate.email =email
			candidate.phone_number = phone_number
			candidate.current_designation= current_designation
			candidate.current_employer=current_employer
			candidate.expected_ctc = expected_ctc
			candidate.notice_period=notice_period
			candidate.total_exp_yrs=total_exp_yrs
			candidate.total_exp_mts=total_exp_mts
			candidate.highest_qual=highest_qual
			candidate.college_highest_qual=college_highest_qual
			candidate.current_location=current_location
			if 'cv' in request.FILES and request.FILES['cv']:
				candidate.cv=request.FILES['cv']
			#candidate.cv = cv
			candidate.save()
			messages.success(request, 'Profile Details Updated Successfully')
			return redirect('index')
		else:
			print "Password didn't match"
	if request.user.is_authenticated():
		login_var=True
	else:
		login_var=False
	return render (request,'recruitment/update_information.html',{'title':'Shanvi Staffing | Update Personal Details','login':login_var,'username':request.user.username,'candidate':candidate})

def signup (request):
	if request.method == 'POST':
		name=request.POST['full_name']
		email=request.POST['email']
		phone_number=request.POST['mobile_no']
		current_designation=request.POST['current_designation']
		current_employer=request.POST['current_employer']
		current_ctc=request.POST['current_salary']
		expected_ctc=request.POST['expected_salary']
		notice_period=request.POST['notice_period']
		total_exp_yrs=request.POST['total_exp_yrs']
		total_exp_mts=request.POST['total_exp_mts']
		highest_qual=request.POST['highest_qual']
		college_highest_qual=request.POST['college_highest_qual']
		current_location=request.POST['current_location']
		cv=request.FILES['cv']
		username=request.POST['username']
		password=request.POST['password']
		user = User.objects.create_user(username=username,password=password)
		candidate = Candidate(user=user,name=name,email=email,phone_number=phone_number,current_designation=current_designation,current_location=current_location,current_ctc=current_ctc,current_employer=current_employer,expected_ctc=expected_ctc,notice_period=notice_period,total_exp_yrs=total_exp_yrs,total_exp_mts=total_exp_mts,highest_qual=highest_qual,college_highest_qual=college_highest_qual,cv=cv)
		candidate.save()
		messages.success(request, 'Your Account Has Been Created !')
		login(request,user)
		return redirect('index')

def requirement (request):
	if request.method=='POST':
		full_name=request.POST['full_name']
		email=request.POST['email_id']
		company_name=request.POST['company_name']
		location=request.POST['location']
		cont_no=request.POST['cont_no']
		job_description=request.POST['job_description']
		further_info=request.FILES['further_info']
		req = Requirement(full_name=full_name,email=email,company_name=company_name,location=location,cont_no=cont_no,job_description=job_description,further_info=further_info)
		req.save()
		messages.success(request, 'Your Requirements Have Been Duly Noted')
		return redirect('index')

def apply_job (request,job_id):
	candidate = request.user
	position = JobOpening.objects.get(pk=job_id)
	status = 'Pending'
	
	application = JobApplication(candidate=candidate,position=position,status=status)
	print application
	application.save()
	messages.success(request, 'Applied Successfully! To view your application => Application Tracking System on the top right corner menu')
	return redirect('joblist')

def change_password (request):
	user = request.user
	if request.user.is_authenticated():
		login_var=True
	else:
		login_var=False
	if request.method == 'POST':
		old_password = request.POST['old_password']
		if authenticate(username=user,password=old_password):
			if request.POST['new_password']==request.POST['confirm_password']:
				user.set_password(request.POST['new_password'])
				user.save()
				#login(request,user)
				messages.success(request,"Password has been changed successfully, please login again")
			else:
				print "New Passwords Do Not Match"
				# Add failure message here
		else:
			print "Old password entered is wrong"
			# Add failure message here
		return redirect('index')
	else:
		return render (request,'recruitment/change_password.html',{'title':'Shanvi Staffing | Change Password','login':login_var,'username':request.user.username})

def app_tracking_sys (request):
	user = request.user
	if request.user.is_authenticated():
		login_var=True
	else:
		login_var=False
	applications = JobApplication.objects.filter(candidate=user)
	return render(request,'recruitment/application_tracking.html',{'title':'Shanvi Staffing | Application Tracking System','login':login_var,'username':request.user.username,'applications':applications})

def logout_view (request):
	logout(request)
	# Add Logout Message Here
	messages.success(request, 'Logged Out Successfully')
	return redirect('index')