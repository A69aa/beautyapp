from django.contrib import admin
from django.urls import path,include
from beautyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/services/', views.ServicesListAPIView.as_view()),
    path('api/v1/services/<int:id>/', views.ServicesUpdateDeleteAPIView.as_view()),
]
