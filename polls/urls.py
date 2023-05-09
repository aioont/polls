from django.urls import re_path, path
from . import views
from django.contrib.auth import views as auth_views

app_name='polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('create-poll/', views.createpoll, name='createpoll'),
    path('view-polls/', views.viewpolls, name='viewpolls'),
    re_path(r'^(?P<question_id>[0-9]+)/$',views.detail, name='detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results$',views.results, name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/votes$',views.vote, name='vote'),
]
