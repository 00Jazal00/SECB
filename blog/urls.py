from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # Require Pages 
    path('blog/<int:id>',views.Blog, name="BlogHome"),
    path('BlogDetail/<str:code>',views.BlogDetail, name="BlogDetail"),
    path('BlogSearch/',views.BlogSearch, name="BlogSearch"),
    
]
