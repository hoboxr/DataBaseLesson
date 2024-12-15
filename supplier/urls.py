#定义了网站的 URL 入口，相当于 "目录" 的作用。它引导你的网页请求到对应的 View
# （在 Django 中，网页请求由一个 URL 到达视图加工处理后，返回对应的网页。URL 与视图之间的对应关系，由 URLConf 做了映射）。
from . import views
from django.urls import path
from .views import show_category

#在模板或者其他应用中引用这个应用的 URL 时可以使用这个名称。
# 例如 {% url 'canteen:canteen' %}。
app_name = 'supplier'

urlpatterns = [
    #当用户访问你的网站的根 URL（例如 http://127.0.0.1:8000/）时，Django 会调用 show_canteen 这个视图函数，
    # 并将其返回的 HTTPResponse 作为 HTTP 响应返回给用户。
    # name 参数为这个 URL 模式命名，这样你就能在模板或视图中使用 {% url 'canteen' %} 这种形式来引用这个 URL。
    # path('', show_canteen, name='canteen'),
    #当用户访问 http://127.0.0.1:8000/shop/ 时，Django 会调用 show_shop 这个视图函数。
    path('', show_category, name='category')
]