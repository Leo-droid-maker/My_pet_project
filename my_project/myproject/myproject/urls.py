from django.contrib import admin
from django.urls import path, include
from myprojectapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('cart/', include('cartapp.urls', namespace='cart')),
    path('men/', include('menapp.urls', namespace='men')),
    path('women/', include('womenapp.urls', namespace='women')),
    # path('single/', include('myprojectapp.urls', namespace='single')),
    path('single/', include('singleapp.urls', namespace='single')),
    path('404/', views.page404, name='404'),
    path('kids/', include('kidsapp.urls', namespace='kids')),

    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', include('adminapp.urls', namespace='admin')),

    path('control/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
