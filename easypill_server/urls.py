"""easypill_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# TODO: 여기 라우터로 추후에 변경할 것

from django.contrib import admin
from django.urls import path, include
from product.views import ProductListAPI, CommentAPI, ProductDetailAPI, UserAPI
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('product', ProductListAPI, basename='product')  # (게시글)
router.register('comment', CommentAPI, basename='comment')  # (댓글)
router.register('user', UserAPI, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('product/<int:pk>/detail', ProductDetailAPI)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path
# from product.views import ProductListAPI, CommentAPI

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/product/', ProductListAPI.as_view()),
#     path('api/comment/', CommentAPI.as_view())
# ]
