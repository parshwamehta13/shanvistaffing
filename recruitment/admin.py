from django.contrib import admin
from .models import JobOpening, Candidate, JobApplication, Requirement
# Register your models here.

class JobAppicationAdmin(admin.ModelAdmin):
	list_display = ('id','candidate','position','application_date','status','comment')

class JobApplicationInline (admin.TabularInline):
	model = JobApplication
	extra = 0

class JobOpeningAdmin (admin.ModelAdmin):
	inlines = [JobApplicationInline]
	list_display = ('id','company_name','position','min_salary','max_salary','location','min_requirement','job_description','posting_date')

class CandidateAdmin (admin.ModelAdmin):
	list_display = ('id','name','email','phone_number','current_designation','current_ctc','current_employer','expected_ctc','notice_period','total_exp_yrs','total_exp_mts','highest_qual','college_highest_qual','current_location','cv')

class RequirementAdmin (admin.ModelAdmin):
	list_display = ('id','full_name','email','company_name','location','cont_no','job_description','further_info')

admin.site.register(JobOpening, JobOpeningAdmin)
admin.site.register(JobApplication, JobAppicationAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Requirement, RequirementAdmin)