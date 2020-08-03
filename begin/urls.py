from django.urls import path
from .views import mainpage,home,aboutus,service,contact
app_name='begin'

urlpatterns=[
    path('',mainpage,name='index'),
    path('home/',mainpage,name='home'),
    path('about-us/',aboutus,name='about-us'),
    path('service/',service,name='service'),
    path('contact/',contact,name='contact')

]