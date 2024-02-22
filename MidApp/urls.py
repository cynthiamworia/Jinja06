from django.urls import path
from MidApp import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Contact/', views.Contact, name='Contact'),
    path('About/', views.AboutUs, name='About'),
    path('Gallery/', views.Gallery, name='Gallery')
]
