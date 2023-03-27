"""avito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads import views
from rest_framework import routers

from ads.views import AnnouncementListViewSet
from category.views import CategoryListViewSet
from users.views import LocationListViewSet

router = routers.SimpleRouter()
router.register(r'ad', AnnouncementListViewSet)
# router.register(r'cat', CategoryListViewSet)

router = routers.DefaultRouter()
router.register(r'location', LocationListViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('ad/', include('ads.urls')),
    path('cat/', include('category.urls')),
    path('users/', include('users.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
