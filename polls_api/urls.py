from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('api/', PollDetailListApiView.as_view(), name='api'),
    path('api/<int:poll_id>/', PollDetailApiViewId.as_view()),

]
