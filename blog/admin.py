from django.contrib import admin

# Register your models here.
from .models import BLOG_POST, BLOG_COMMENT
@admin.register(BLOG_POST)
class BLOG_POSTAdmin(admin.ModelAdmin):
    list_display = ('title','type','topic')    
    search_fields = ['code','title', 'type']
    fieldsets = [
        ('Unique (Don\'t edit)', {
            'classes': ['collapse'],
            'fields': ['code'],
        }),
        ('Header Fields', {
            'fields': ['type','text','picture','video','quote_header','quote_writer_name'],
        }),
        ('Main Fields', {
            'classes': ['collapse'],
            'fields': ['topic','title','publish_date','description'],
        }),
    ]


@admin.register(BLOG_COMMENT)
class BLOG_COMMENTAdmin(admin.ModelAdmin):
    list_display = ('name','email','website')    
    search_fields = ['name','email','website','code']
    fieldsets = [
        ('Unique (Don\'t edit)', {
            'classes': ['collapse'],
            'fields': ['code'],
        }),
        ('Header Fields', {
            'fields': ['name','email','website','message','permission'],
        }),
    ]
