from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User

class CoachAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'gender', 'skype', 'description')
	list_filter = ['user__is_staff']
	search_fields = ['user__first_name', 'user__last_name', 'gender', 'skype', 'description']

admin.site.register(Coach, CoachAdmin)
