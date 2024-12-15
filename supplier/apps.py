#要用来配置这个 app 。比如 app 的名字，还有一些相关的设置。

#这行代码导入了 Django 的 AppConfig 类， 这个类是每一个应用配置类的基类。
from django.apps import AppConfig

#自定义一个应用的配置类，命名为 CanteenConfig，继承自 AppConfig。
class CanteenConfig(AppConfig):
    #这行代码指定了模型自动创建的主键的类型，类型被设置为 BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    #规定了这个应用的名字为 'canteen'，其对应的是应用的标准的全 Python 路径
    name = 'supplier'
    # 在 Django admin 中显示
    verbose_name = '供应商'
