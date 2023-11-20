from django.contrib import admin

from .models import *

admin.site.register(Category)


class AnswerAdmin(admin.StackedInline):
      model=Answer
      
      
class QestionAdmin(admin.ModelAdmin):
      inlines=[AnswerAdmin]

admin.site.register(Question,QestionAdmin)
admin.site.register(Answer)