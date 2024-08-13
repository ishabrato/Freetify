from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='index'),
    path('about', views.about, name='about'),
    path('player', views.myPlayer, name='home'),
    path('signin', views.loginUser, name='login'),
    path('signup', views.regUser, name='register'),
    path('logout', views.logoutUser, name='logout')

]
