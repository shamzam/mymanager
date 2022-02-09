from django.urls import path

from . import views

app_name = 'pull'
urlpatterns = [
    path('', views.login, name='login'),
]
