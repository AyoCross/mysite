from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('问题描述', max_length=200)
    pub_date = models.DateTimeField('发表时间')
    just_test = models.CharField('用于测试', max_length=120)

    @staticmethod
    def even_text(value):
        if value % 2 != 0:
            raise ValueError("%d 不能被2来 整除！" % value)

    # even_field = models.IntegerField('测试过滤器的作用', validators=[even_text])

    class Meta:
        app_label = 'polls'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):  # 关于这些方法属性的更多信息，参见 list_display。
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布？'


class Choice(models.Model):
    question = models.ForeignKey(Question)  # '问题',
    choice_text = models.CharField(max_length=200)  # '问题描述',
    votes = models.IntegerField(default=0)  # '投票',

    def __str__(self):
        return self.choice_text
