from django.urls import path

from . import views

app_name = 'explorer'

urlpatterns = [
    path('', views.CollectionsList.as_view(), name='collections'),
    path('fetch/', views.FetchData.as_view(), name='fetch'),


]