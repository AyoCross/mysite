"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  # 使用include的时候，前面的正则没有$，
    url(r'^polls/', include('polls.urls', namespace='polls')),  # 因为include会把这之前的处理掉，把剩下的传过去
]  # 命名空间是用来在模板中区分同名的视图情况，比如：
# <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
# 改为带有命名空间：<li><a href="{% url 'polls:detail' question.id %}">
