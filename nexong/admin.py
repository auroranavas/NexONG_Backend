from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Educator)
admin.site.register(Meeting)
admin.site.register(Family)
admin.site.register(Student)
admin.site.register(Partner)
admin.site.register(Volunteer)
admin.site.register(EducationCenter)

