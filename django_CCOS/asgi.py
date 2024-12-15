"""
ASGI config for django_CCOS project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# 提供了一些与操作系统交互的函数，例如文件和目录操作
import os

#这个函数可以创建一个适用于 ASGI 服务器的 Django 应用程序实例。
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_CCOS.settings')

application = get_asgi_application()
