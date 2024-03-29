from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# admin.site.register(Question)
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
    ('Date information', {'fields':['pub_date']})]

    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
