from django.urls import path, include
from lookup import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),

]
