# 初始化polls应用
from django.contrib import admin, auth

admin.default_app_config = 'polls.apps.AdminConfig'
auth.default_app_config = 'polls.apps.AuthConfig'
default_app_config = 'polls.apps.PollsConfig'


