from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import NEWSLETTER
# Create your views here.

def Home(request):
    # Adding news letter
    news_msg = False
    if request.method == 'POST':
        newsletter  = request.POST['newsletter']
        # Testing if email is already exit
        find_Newsletter =NEWSLETTER.objects.filter(email=newsletter).first()
        if find_Newsletter == None:
            NEWSLETTER(email=newsletter).save()
            news_msg = True



    return render(request, 'home.html', {'news_msg':news_msg})




    