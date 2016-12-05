<<<<<<< HEAD
from django.contrib import admin
from .models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}



admin.site.register(Course, CourseAdmin)
=======
from django.contrib import admin

from .models import (Course, Enrollment, Announcement, Comment, Lesson,
    Material)


class CourseAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class MaterialInlineAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
>>>>>>> f2e683044aaafdb905a72a34bad0582a9ae5a7ed
