from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.utils.timezone import now
# Blog Post
TYPE  = (
    ('text','text'),
    ('image','image'),
    ('video', 'video'),
    ('quote', 'quote'),
)
class BLOG_POST(models.Model):
    # Unique fields
    id = models.AutoField(primary_key=True, editable=True, unique=True)
    code = models.CharField(max_length=100, default=uuid.uuid4, help_text="No need to edit this field.")
    comment = models.IntegerField(default=0)
    # header field
    type = models.CharField(max_length=50, choices=TYPE, default='image')
    text = RichTextField(blank=True, null=True)
    picture = models.ImageField(upload_to='images/blog', default="", blank = True)
    video = models.TextField( default="", help_text="Paste a video video iframe link.", blank = True)
    quote_header = models.CharField(max_length=1000, default="", blank = True)
    quote_writer_name = models.CharField(max_length=100, default="", blank = True)
    # Main fields
    topic = models.CharField(max_length=100, default="", blank = True)
    title = models.CharField(max_length=500, default="", blank = True)
    publish_date = models.DateTimeField(default=now)
    description = RichTextField(blank=True, null=True)

class BLOG_COMMENT(models.Model):
    # Unique fields
    id = models.AutoField(primary_key=True, editable=True, unique=True)
    code = models.CharField(max_length=100, default="", help_text="No need to edit this field.")


    quote_header = models.CharField(max_length=1000, default="", blank = True)
    quote_writer_name = models.CharField(max_length=100, default="", blank = True)
    # Main fields
    name = models.CharField(max_length=100, default="", blank = True)
    email = models.CharField(max_length=500, default="", blank = True)
    website = models.CharField(max_length=500, default="", blank = True)
    message = models.TextField(default="", blank=True)
    permission = models.CharField(max_length=500, default="", blank = True)


