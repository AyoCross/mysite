from django.contrib import admin
from django.contrib.auth.apps import AuthConfig as MyAuthConfig
from django.contrib.admin.apps import AdminConfig as MyAdminConfig
from django.apps import AppConfig


class AuthConfig(MyAuthConfig):
    name = 'django.contrib.auth'
    verbose_name = u'用户管理'


class AdminConfig(MyAdminConfig):
    name = 'django.contrib.admin'
    verbose_name = u'后台管理'


class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name = u'投票系统app'

