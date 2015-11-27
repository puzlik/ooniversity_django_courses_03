from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
	model = Lesson
	#list_display = ('subject', 'description', 'order')
	list_display = (('subject', 'description', 'order'), )

class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'short_description')
	inlines = [LessonInline, ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
