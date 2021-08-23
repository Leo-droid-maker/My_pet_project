from django.urls import path
from menapp import views


app_name = 'menapp'

urlpatterns = [
    # path('', views.Men_view.as_view(), name='men'),
    # path('category/<int:pk>/', views.Men_view.as_view(), name='men_category')
    path('', views.men, name='men'),
    path('category/<int:pk>/', views.men, name='men_category'),
]
