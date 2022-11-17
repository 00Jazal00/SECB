from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# All Models
from .models import NEWSLETTER, CONTACT, JOB

# For E-mails
from django.template import loader
from django.core.mail import EmailMultiAlternatives

# Bot working

# START FROM THERE:  just create a remplate and add to "update" txt file delete update model GoodLuck : )


def Bot(request):
    if request.user.is_superuser:
        Task = []
        # Sending Update email to all
        for j in NEWSLETTER.objects.all():
            try:
                template = loader.get_template(
                    'mails/update.txt')
                context = {
                    'msg': 'Nothing',
                }
                message = template.render(context)
                email = EmailMultiAlternatives(
                    "Find out updates", message,
                    "SECB"+" Jobs & Scholarships",
                    [f'{j.email}']
                )
                email.content_subtype = 'html'
                email.send()
            except:
                Task.append(f'Some Error In ({j.email})')
        return HttpResponse(f'Successfully Completed :)\nWhat Bot did? \nTask Completed >> {Task}')
    else:
        return HttpResponseRedirect("/")


def Home(request):
    # Adding news letter
    news_msg = False
    if request.method == 'POST':
        newsletter = request.POST['newsletter']
        # Testing if email is already exit
        find_Newsletter = NEWSLETTER.objects.filter(email=newsletter).first()
        if find_Newsletter == None:
            NEWSLETTER(email=newsletter).save()
            news_msg = True

    return render(request, 'home.html', {'news_msg': news_msg})


def Contact(request):
    success = ""
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        code = request.POST['code']
        CONTACT(code=code, name=name, subject=subject, email=email, phone_number=phone_number, message=message).save()
        success = 'Successfully Send!'
    return render(request, 'require/contact.html', {'success':success})



def Jobs(request):
    jobs = JOB.objects.all()
    all = JOB.objects.all()
    remote = JOB.objects.filter(type='Remote')
    foreign = JOB.objects.filter(type='Foreign') 
    Pakistan = JOB.objects.filter(type='Pakistan')
    return render(request, 'require/jobs.html', {'jobs': jobs, 'all':all, 'remote':remote, 'foreign':foreign, 'pakistan':Pakistan})


def jobViewMore(request, type):
    if type != 'All':
        jobs = JOB.objects.filter(type=type)
    else:
        jobs = JOB.objects.all()
    return render(request, 'require/jobs/jobViewMore.html', {'jobs':jobs, 'type':type})

def JobDetail(request, code):
    details = JOB.objects.filter(code=code).first()
    skills = details.require_knowledge_skills_abilities.split('$$$')
    experience = details.education_experience.split('$$$')
    related_jobs = JOB.objects.filter(type=details.type)
    return render(request, 'require/jobs/jobs_details.html', {'details':details, 'skills':skills, 'experience':experience, 'related_jobs':related_jobs})