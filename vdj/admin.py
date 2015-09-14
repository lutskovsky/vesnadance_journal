from django.contrib import admin
from .models import *
# Register your models here.

class TaughtByInline(admin.TabularInline):
    model = TaughtBy
    extra = 1


class LessonAdmin(admin.ModelAdmin):
    inlines = (TaughtByInline,)

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Venue)
admin.site.register(Student)
admin.site.register(Lesson, LessonAdmin)
