from django.urls import path
from womenapp import views


app_name = 'menapp'

urlpatterns = [
    path('', views.women, name='women'),
    path('category/<int:pk>/', views.women, name='women_category'),
]