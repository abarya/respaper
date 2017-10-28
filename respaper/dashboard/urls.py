from django.conf.urls import url
from . import views

app_name="dashboard"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^thread_index/',views.thread_index,name="thread_index"),
]