from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):  # Question모델에 세부 기능 추가
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)  # Question 모델 등록
admin.site.register(Answer)