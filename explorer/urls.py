from django.urls import path

from . import views

app_name = 'explorer'

urlpatterns = [
    path('', views.CollectionsList.as_view(), name='collections'),
    path('fetch/', views.FetchData.as_view(), name='fetch'),
    path('details/<pk>', views.CollectionDetails.as_view(), name='details'),
    path('details/<pk>/json-details/<int:num_posts>/', views.CollectionJSONDetails.as_view(), name='json-details'),

]