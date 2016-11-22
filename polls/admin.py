from django.contrib import admin
from .models import Question
from .models import Choicess
from django.utils.timezone import now
from django.http import HttpResponse
from django.core import serializers


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response
export_as_json.short_description = 'try!'


class ChoiceInline(admin.TabularInline):  # StackedInline  TabularInline
    model = Choicess
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    actions = [export_as_json, 'status_setD', 'status_setY', 'status_setZ']  # 按照先后顺序

    def status_setZ(self, request, queryset):
        row_update = queryset.update(status='Z')
        self.message_user(request, "共有%s个question被改为正在处理。%d" % (row_update, now().month))

    def status_setY(self, request, queryset):
        row_update = queryset.update(status='Y')
        self.message_user(request, "共有%s个question被改为已处理完。%d" % (row_update, now().month))

    def status_setD(self, request, queryset):
        row_update = queryset.update(status='D')
        self.message_user(request, "共有%s个question被改为等待处理。%d" % (row_update, now().month))  # actions完成后出现提示信息。
    status_setD.short_description = '状态：等待处理'
    status_setY.short_description = '状态：已处理'
    status_setZ.short_description = '状态：正在处理'

    def get_ques_state(self, obj):
        if obj.pub_date.month != now().month:
            return u'<span style="color:red;font-weight:bold">%s</span>' % ("之前发表的",)
        else:
            return u'<span style="color:green;font-weight:Arial">%s</span>' % ("这个月",)
    get_ques_state.short_description = '是否这个月发表'
    get_ques_state.allow_tags = True

    # 在自定义的manager类中重写get_queryset()， 下面这句没什么用
    model = Question.objects.filter(pub_date__startswith='1')  # month=now().month

    fieldsets = [
        ('详细信息',    {'fields': ('pub_date', 'just_test'), 'classes': ('collapse',)}),  # 实现hide效果
        ('问题TEXT',    {'fields': ('question_text', 'status')}),
        # fields的顺序就是按照这个来
    ]
    inlines = [ChoiceInline]
    list_per_page = 10
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 被下面函数顶替了
    list_filter = ['pub_date', 'status']
    search_fields = ['question_text']  # 麻蛋我就说怎么不起作用，漏了s...
    ordering = ('-pub_date',)  # 排序

    def get_list_display(self, request):  # ModelAdmin中一般有两种表达形式，函数的表达形式优先级高于变量
        return ['question_text', 'pub_date', 'status', 'get_ques_state']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
