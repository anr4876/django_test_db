from django.urls import path
from . import views


urlpatterns = [
    path('testdb/', views.getTestDatas, name='test01datas')
]