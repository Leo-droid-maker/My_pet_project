from django.urls import path
from cartapp import views

app_name = 'cartapp'

urlpatterns = [
    path('', views.cart, name='view_cart'),
    path('add_to_cart/<int:pk>/', views.cart_add, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.cart_remove, name='remove_from_cart'),
    path('edit/<int:pk>/<int:quantity>/', views.cart_edit, name='edit')
]
