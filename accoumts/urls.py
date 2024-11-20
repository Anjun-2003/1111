from django.urls import path
from . import views

urlpatterns = [
    path('signupaccoumt/' , views.signupaccoumt, name='signupaccoumt'),
    path('logout/', views.logoutaccoumt, name='logoutaccoumt'),
    path('login/', views.loginaccoumt, name='loginaccoumt'),
]
