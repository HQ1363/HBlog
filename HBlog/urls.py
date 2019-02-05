"""HBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

from blog.views import user_login, user_logout, query_user_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # get token
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/user/login$', user_login),
    url(r'^api/user/logout$', user_logout),
    url(r'^api/user/profile$', query_user_profile),
    url(r'^api/blog/', include("blog.urls"), name="blog"),
    url(r'^api-docs', include_docs_urls(title=u"HBlog", permission_classes=())),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
