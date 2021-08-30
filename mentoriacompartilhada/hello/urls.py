from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('pessoas', views.pessoa_list),
    path('pessoas/<int:pk>', views.pessoa_details),
    path('hello',views.hello)
]





