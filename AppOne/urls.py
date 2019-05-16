from django.urls import path
from AppOne import views


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup')

]

