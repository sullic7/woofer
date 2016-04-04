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
from woofer.views import home_views, user_views, dog_views, event_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.index, name='home'),
    url(r'^index/$', home_views.index, name='index'),
    
    # User URLs
    url(r'^login/$', user_views.login_view, name='login'),
    url(r'^logout/$', user_views.logout_view, name='logout'),
    url(r'^create_user/$', user_views.create_user, name='create-user'),
    url(r'^view_user/(?P<userid>[0-9]+)/$', user_views.view_user, name='view-user'),
    url(r'^edit_user/(?P<userid>[0-9]+)/$', user_views.edit_user, name='edit-user'),
    
    # Dog URLs
    url(r'^dog_view/(?P<dogid>[0-9]+)/$', dog_views.dog_view, name='view-dog'),
    # url(r'^add_dog/$', dog_views.edit_dog, name='add-dog'),
    url(r'^edit_dog/(?P<dogid>[0-9]+)/$', dog_views.edit_dog, name='edit-dog'),
    
    # Event URLs
    url(r'^event_edit/(?P<eventid>[0-9]+)/$', event_views.edit_event, name='edit-event'),
    url(r'^event_view/(?P<eventid>[0-9]+)/$', event_views.view_event, name='view-event'),
    url(r'^event_list/$', event_views.view_event_list, name='event-list'),
    url(r'^create_event/$', event_views.create_event, name='create-event')
    
]