# coding:utf-8
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Question
from django.shortcuts import render, get_object_or_404
# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # 筛选出需要的条件
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return render(request, 'polls/index.html',context)  # 二者皆可
    return HttpResponse(template.render(context))
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id) # 通过主键获取数据
    #     print u'找到了question %s'%(question_id)
    # except Question.DoesNotExist:
    #     print u'没找到question %s'%(question_id)
    #     raise Http404("Question does not exist")    # 返回404错误
    question = get_object_or_404(Question, pk=question_id)  # 相当于获取对象或者返回404
    return render(request, 'polls/detail.html', {'question':question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
