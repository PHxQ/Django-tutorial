# coding:utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),    # name 在后面的 url 设置里面很有作用
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/specifics/12/
    # url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail')   # 仅仅修改 url 而不需要修改 template
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
