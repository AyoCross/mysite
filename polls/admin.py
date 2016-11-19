from django.contrib import admin
from .models import Question
from .models import Choice


class ChoiceInline(admin.TabularInline):  # StackedInline  TabularInline
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['question_text']}),
        ('数据信息',    {'fields': ['pub_date'], 'classes': ['collapse']}),  # 实现hide效果
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_field = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
