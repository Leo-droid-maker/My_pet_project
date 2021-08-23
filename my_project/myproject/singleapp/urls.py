from django.urls import path
from singleapp import views
from myprojectapp import views as main_page_view


app_name = 'singleapp'

urlpatterns = [
    path('', main_page_view.main, name='single'),
    path('product/<int:pk>/', views.single, name='product'),
]
