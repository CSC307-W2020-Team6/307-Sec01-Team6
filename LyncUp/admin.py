# from .models import Question #this line added
# admin.site.register(Question)#this line added

# Register your models here.
# from django.contrib import admin
# from .models import Choice, Question
#
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#             (None,               {'fields': ['question_text']}),
#             ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#                 ]
#     inlines = [ChoiceInline]
#
# admin.site.register(Question, QuestionAdmin)

from django.contrib import admin
from .models import Post

admin.site.register(Post)