from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.utils.timezone import now
    # text = RichTextField(blank=True, null=True)



# Save all subscribe user email
class NEWSLETTER(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, default="")
    def __str__(self):                                  
        return self.email

# User Contact US
class CONTACT(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100, default="")
    message = models.TextField(default="")

TIME  = (
    ('Temporary','Temporary'),
    ('Part-time', 'Part-time'),
    ('Full-time', 'Full-time'),
    ('Freelance', 'Freelance'),
    ('Goverment', 'Goverment'),
    ('Private', 'Private'),
)

TYPE = (
    ('All','All'),
    ('Remote','Remote'),
    ('Foreign', 'Foreign'),
    ('Pakistan', 'Pakistan'),
)
GENDER  = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Male - Female', 'Male - Female'),
)
# User Jobs
class JOB(models.Model):
    # Unique fields
    id = models.AutoField(primary_key=True, editable=True, unique=True)
    code = models.CharField(max_length=100, default=uuid.uuid4, help_text="No need to edit this field.")
    # Jobs Box Values
    picture = models.ImageField(upload_to='images/jobs', default="", blank = True)
    name = models.CharField(max_length=100, default="", blank = True)
    type = models.CharField(max_length=50, choices=TYPE, default='All', blank = True)
    timing = models.CharField(max_length=50, choices=TIME, default='Private', blank = True)
    company = models.CharField(max_length=100, default="", blank = True)
    out_location = models.CharField(max_length=100, default="", blank = True)
    out_category = models.CharField(max_length=100, default="", blank = True)

    # Jobs Details (Short)
    title = models.CharField(max_length=100, default="", blank = True)
    location = models.CharField(max_length=100, default="", blank = True)
    phone_number = models.CharField(max_length=100, default="", blank = True)
    email = models.CharField(max_length=100, default="", blank = True)
    publish_date = models.DateTimeField(default=now)
    expire_date = models.DateTimeField(default=now)
    website_link = models.CharField(max_length=100, default="", blank = True)
    map = models.TextField( default="", help_text="Paste link from the google map.", blank = True)
    applications = models.CharField(max_length=100, default="", blank = True)
    visitors = models.CharField(max_length=100, default="0", help_text="Original value will be add in your value.", blank = True)
    remaining_days = models.CharField(max_length=100, default="0", help_text="Original value will be add in your value.", blank = True)

    # Deep Details For User
    salary = models.CharField(max_length=100, default="", blank = True)
    gender = models.CharField(max_length=50, choices=GENDER, default='Male - Female')
    career_level = models.CharField(max_length=100, default="", blank = True)
    industry = models.CharField(max_length=100, default="", blank = True)
    experience = models.CharField(max_length=100, default="", blank = True)
    qualifications = models.CharField(max_length=100, default="", blank = True)
    jobs_descriptions = RichTextField(blank=True, null=True)
    require_knowledge_skills_abilities = models.TextField(default="", help_text="Break point with ($$$)", blank = True)
    education_experience = models.TextField(default="", help_text="Break point with ($$$)", blank = True)
   




