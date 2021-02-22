from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
]
