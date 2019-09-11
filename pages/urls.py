from django.urls import path 
from . import views

# domain.com/pages/__
urlpatterns = [
    path('', views.index),
    path('greeting/<str:name>/', views.greeting),
]
