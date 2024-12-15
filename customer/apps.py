from django.apps import AppConfig


class CustomerConfig(AppConfig):
    #这行设置的意思是：除非你在模型中明确指定主键，否则 Django 会为你的模型添加一个 BigAutoField 类型的 id 字段作为主键。
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer'
    verbose_name = '顾客'
