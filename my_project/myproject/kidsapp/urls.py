from django.urls import path
from django.urls.conf import path
from kidsapp import views

app_name = 'kidsapp'

urlpatterns = [
    path('', views.kids, name='kids'),
    path('category/<int:pk>/', views.kids, name='kids_category'),
]
