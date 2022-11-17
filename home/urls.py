from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # Require Pages 
    path('',views.Home, name="HomePage"),
    path('contact/',views.Contact, name="Contact"),
    path('jobs/',views.Jobs, name="Jobs"),
    path('jobViewMore/<str:type>',views.jobViewMore, name="jobViewMore"),
    path('jobDetail/<str:code>',views.JobDetail, name="JobDetail"),





    # Process that need to auto complete
    path('bot/',views.Bot, name="Bot"),

]
