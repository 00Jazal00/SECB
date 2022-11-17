from turtle import update
from django.contrib import admin

# Register your models here.
from .models import NEWSLETTER, CONTACT, JOB




@admin.register(JOB)
class JOBAdmin(admin.ModelAdmin):
    list_display = ('name','company','salary','visitors','expire_date','timing','type')
    search_fields = ['code','name','company','salary','expire_date','timing', 'type']
    fieldsets = [
        ('Unique (Don\'t edit)', {
            'classes': ['collapse'],
            'fields': ['code'],
        }),
        ('Date (Publish & Expire)', {
            'classes': ['collapse'],
            'fields': ['publish_date', 'expire_date'],
        }),
        (None, {
            'fields': ['picture','name','type','timing','company','out_location','out_category'],
        }),
        ('Jobs Details (Short)', {
            'classes': ['collapse'],
            'fields': ['title','location','phone_number','email','website_link','map', 'applications','visitors','remaining_days'],
        }),
        ('Deep Details For User', {
            'classes': ['collapse'],
            'fields': ['salary','gender','career_level', 'industry','experience','qualifications', 'jobs_descriptions', 'require_knowledge_skills_abilities','education_experience'],
        }),
    ]




















# admin.site.register(CONTACT)
@admin.register(CONTACT)
class CONTACTAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject")


# Hide model because admin don't need this, Model is used to edit password of user
def register_hidden_models(*model_names):
    for m in model_names:
        ma = type(
            str(m)+'Admin',
            (admin.ModelAdmin,),
            {
                'get_model_perms': lambda self, request: {}
            })
        admin.site.register(m, ma)

register_hidden_models(NEWSLETTER)