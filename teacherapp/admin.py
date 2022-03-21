from django.contrib import admin

from teacherapp.models import Faq, Jobs, Members, Notifications

# Register your models here.
# admin.site.register(TeacherData)
admin.site.register(Notifications)
admin.site.register(Faq)
admin.site.register(Members)
admin.site.register(Jobs)