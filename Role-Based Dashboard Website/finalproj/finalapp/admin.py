from django.contrib import admin
from .models import Parent,Faculty,Transaction,Student
# Register your models here.
admin.site.register(Parent)

admin.site.register(Transaction)
admin.site.register(Student)
admin.site.register(Faculty)