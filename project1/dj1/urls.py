from django.urls import path,include
from dj1 import views

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.home),
    path('login/',views.login),
    path('details',views.details),
]