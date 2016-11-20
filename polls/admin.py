from django.contrib import admin
from .models import Question
from .models import Choice
import datetime
from django.utils.timezone import now


class ChoiceInline(admin.TabularInline):  # StackedInline  TabularInline
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):

    # model要实现的功能：只显示pub_date = 11的对象，灵感来自于只显示管理员的帖子。
    model = Question.objects.filter(pub_date__month=now().month)
    fieldsets = [
        (None,          {'fields': ('question_text',)}),
        ('详细信息',    {'fields': ('pub_date', 'just_test'), 'classes': ('collapse',)}),  # 实现hide效果
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 被下面函数顶替了
    list_filter = ['pub_date']
    search_field = ['question_text']

    def get_ques_state(self, obj):
        if obj.pub_date.month != now().month:
            return u'<span style="color:red;font-weight:bold">%s</span>' % ("之前发表的",)
        else:
            return u'<span style="color:green;font-weight:Arial">%s</span>' % ("这个月",)

    get_ques_state.short_description = '是否这个月发表'
    get_ques_state.allow_tags = True

    def get_list_display(self, request):  # ModelAdmin中一般有两种表达形式，函数的表达形式优先级高于变量
        return ['question_text', 'pub_date', 'get_ques_state']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
