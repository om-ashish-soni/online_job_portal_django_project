from django.contrib import admin
admin.autodiscover()
from .models import User,Application,Applicant
admin.site.register(User)
admin.site.register(Application)
admin.site.register(Applicant)