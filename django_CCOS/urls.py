

from django.contrib import admin
from django.urls import path

# 用于 include 其他模板所在的 url
from django.conf.urls import include

# 用于 图片 静态存储
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('supplier.urls')),
    path('customer/', include('customer.urls')),
    path('', include('product.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)