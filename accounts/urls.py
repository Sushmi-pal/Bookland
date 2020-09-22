from django.urls import path
from .views import LoginView,ProfileView,SignupView,LogoutView

app_name='accounts'
urlpatterns=[
    path('login/',LoginView,name='login'),
    path('profile/',ProfileView,name='profile'),
    path('signup/',SignupView,name='signup'),
    path('logout/',LogoutView,name='logout'),


]