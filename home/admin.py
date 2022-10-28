from django.contrib import admin

# Register your models here.
from .models import NEWSLETTER

# admin.site.register(Mian_User)

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