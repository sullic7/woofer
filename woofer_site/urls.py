"""woofer_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from woofer import views as woofer_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', woofer_views.index, name='home'),
    url(r'^index$', woofer_views.index, name='index'),
    url(r'^login$', woofer_views.login, name='login'),
    url(r'^logout', woofer_views.logout_view, name='logout'),
    url(r'^create_user', woofer_views.create_user, name='create-user'),
    url(r'^index$', woofer_views.index),
    url(r'^user_view$', woofer_views.user_view),
    url(r'^dog_view$', woofer_views.dog_view),
    url(r'^event_view$', woofer_views.event_view)
]