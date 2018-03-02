from django.contrib import admin
from djangoApp.models import Topic, AccessRecords, Webpage, User
# Register your models here.


admin.site.register(Topic)
admin.site.register(AccessRecords)
admin.site.register(Webpage)
admin.site.register(User)
