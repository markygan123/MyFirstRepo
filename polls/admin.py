from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	fieldsets = [
	   ('Date Information', 		{'fields': ['pub_date'], 'classes': ['collapse']}),
	   (None,						{'fields': ['question']}), 	
	]

	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_field = ['question']


admin.site.register(Poll, PollAdmin)

