from django.urls.conf import path

from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('rull/', views.rull, name='rull'),
    path('gett/', views.gett, name='gett'),
    path('live/', views.live, name='live'),
    path('logo/', views.logo, name='logo'),
    path('index/', views.index, name='index'),
    path('pergramme/', views.pergramme, name='pergramme'),
    ]