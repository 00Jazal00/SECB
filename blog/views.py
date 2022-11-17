from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from math import ceil

# All Models of Blog
from .models import BLOG_POST, BLOG_COMMENT
# Create your views here.
def Blog(request, id):
    n = 0
    get = (id-1)*5
    posts = []
    for i in range(0, 5):
        post = BLOG_POST.objects.filter(id=get+n).first()
        n += 1
        posts.append(post)
    length = len(BLOG_POST.objects.all())
    buttons = ceil(length/5) +1
    disableBtn = buttons - 1
    recent_post = BLOG_POST.objects.all().order_by('-publish_date')
    return render(request, 'blog/blog.html', {'all_post':posts, "buttons":range(1, buttons), 'id':id, 'disableBtn':disableBtn, 'recent_post':recent_post})


def BlogDetail(request, code):
    post = BLOG_POST.objects.filter(code=code).first()
    next = None
    prev = None
    if BLOG_POST.objects.filter(id=post.id+1).first() != None:
        next = BLOG_POST.objects.filter(id=post.id+1).first()
    if BLOG_POST.objects.filter(id=post.id-1).first() != None:
        prev = BLOG_POST.objects.filter(id=post.id-1).first()
    related = BLOG_POST.objects.filter(topic=post.topic)
    success = ""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        message = request.POST['message']
        permission = request.POST['permission']
        post.comment = post.comment +1
        post.save()
        BLOG_COMMENT(code=code ,name=name, email=email, website=website, message=message, permission=permission).save()
        success = 'Successfully Send!'
    comments = BLOG_COMMENT.objects.filter(code=post.code)    
    recent_post = BLOG_POST.objects.all().order_by('-publish_date')
    return render(request, 'blog/blogDetail.html', {'post':post, 'next':next, 'prev':prev, 'related':related, 'success':success, 'comments':comments, 'recent_post':recent_post})

def BlogSearch(request):
    recent_post = BLOG_POST.objects.all().order_by('-publish_date')
    search_posts = BLOG_POST.objects.all()
    posts =''
    if request.method == "POST":
        search = request.POST['search']
        posts = BLOG_POST.objects.filter(title__contains=search)
    return render(request, 'blog/blogSearch.html', {'all_post':posts, 'recent_post':recent_post, "search_posts":search_posts})