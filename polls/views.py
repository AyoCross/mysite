from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
# from django.template import RequestContext, loader

from .models import Question, Choicess


# 使用通用视图来实现
class IndexView(generic.ListView):
    '''载入polls/index.html模板，并传给它一个context。
    Context是一个字典，将模板变量的名字映射到Python 对象。'''
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        ''':return the last five published questions.'''
        return Question.objects.order_by('-pub_date')[:3]
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}  # 快捷方式
    # return render(request, 'polls/index.html', context)


class DetailView(generic.DetailView):
    model = Question  # 作用于哪个模型
    template_name = 'polls/detail.html'  # 指定一个html模板


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choicess_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
