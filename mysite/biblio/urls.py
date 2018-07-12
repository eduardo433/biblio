from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.livro_list, name='livro_list'),
]