from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('signup/', views.signup, name='signup'),
    re_path('login/', views.login, name='login'),
]
