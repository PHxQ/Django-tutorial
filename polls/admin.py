# coding: utf-8
from django.contrib import admin
from .models import Question, Choice
# class ChoiceInline(admin.StackedInline):  # 这个会让问题各个属性都占用一行
class ChoiceInline(admin.TabularInline):    # 一个问题之占用一行
    model = Choice
    extra = 3   # 额外显示 3 个位置
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#    fields = ['question_text','pub_date', ]   # 可以更换显示顺序
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]    # 在Question 内部现实Choice
    list_display = ('question_text', 'pub_date', 'was_published_recently')    # 问题列表显示的信息
    list_filter = ['pub_date']  # 添加了筛选的大体功能,右边的三天内，七天内
    search_fields = ['question_text']   # 添加了过滤的筛选框

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice) # 但是这样Choice就在Question外面了
