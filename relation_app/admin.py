from django.contrib import admin

# Register your models here.

from relation_app.models import College, Principle, Department, Student, Subject

admin.site.register([College, Principle, Department, Student, Subject])
