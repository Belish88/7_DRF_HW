from django.contrib import admin

from school.models import Course, Lesson, Payments


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'course', 'lesson', 'date', 'pay', 'method')
