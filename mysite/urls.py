"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from polls_api import urls as poll_urls 

app_name='polls'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('polls.urls', 'polls'), namespace='polls')),
    path('api-auth/', include('rest_framework.urls')),
    path('polls-detail/', include((poll_urls, 'polls-detail'), namespace='polls-detail')),

    #path('', include(('polls.urls'), namespace='polls')),
   # in index.html "polls:detail"
   # re_path(r'^polls/', include('polls.urls'),namespace='polls'),

]
