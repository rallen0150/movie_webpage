"""movie_webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from movieratings.views import index_view, top_20_view, movie_view, user_view, rater_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view),
    url(r'^top_20_movies/$', top_20_view),
    url(r'^movies/$', movie_view),
    url(r'^users/$', user_view),
    url(r'^rater/(?P<rater_id>\d+)/$', rater_info)
]
