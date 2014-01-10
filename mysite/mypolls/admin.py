from django.contrib import admin
from mypolls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [('Poll Question',{'fields':['question',]}),
        ('Date Info',{'fields':['pub_date',], 'classes':['collapse',]})]
    
    inlines = [ChoiceInline,]
    
    list_display = ['question','pub_date', 'was_published_recently']
    list_filter = ['pub_date',]
    search_fields = ['question',]
    date_hierrachy = ['pub_date']
    
    

admin.site.register(Poll, PollAdmin)
