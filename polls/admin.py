from django.contrib import admin
from .models import Question
from .models import Choicess
import datetime
from django.utils.timezone import now


class ChoiceInline(admin.TabularInline):  # StackedInline  TabularInline
    model = Choicess
    extra = 2


class QuestionAdmin(admin.ModelAdmin):

    # model要实现的功能：只显示pub_date = 11的对象，灵感来自于只显示管理员的帖子。********尝试使用manager.py
    # 在自定义的manager类中重写get_queryset()
    model = Question.objects.filter(pub_date__startswith='1')  # month=now().month

    fieldsets = [
        ('详细信息',    {'fields': ('pub_date', 'just_test'), 'classes': ('collapse',)}),  # 实现hide效果
        ('问题TEXT',    {'fields': ('question_text',)}),
        # fields的顺序就是按照这个来
    ]
    inlines = [ChoiceInline]
    list_per_page = 10
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 被下面函数顶替了
    list_filter = ['pub_date', 'question_text']
    search_fields = ['question_text']  # 麻蛋我就说怎么不起作用，漏了s...
    ordering = ('-pub_date',)  # 排序

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
