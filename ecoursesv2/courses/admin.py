from django.contrib import admin
from .models import Course, Category, Lesson


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
