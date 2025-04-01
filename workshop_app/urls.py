from django.urls import path
from . import views

urlpatterns = [
    path('', views.workshop_list, name='workshop_list'),
    path('<int:pk>/', views.workshop_detail, name='workshop_detail'),
    path('create/', views.workshop_create, name='workshop_create'),
    path('<int:pk>/update/', views.workshop_update, name='workshop_update'),
    path('<int:pk>/delete/', views.workshop_delete, name='workshop_delete'),
    path('api/', views.workshop_list_api, name='workshop_list_api'),
    path('api/<int:pk>/', views.workshop_detail_api, name='workshop_detail_api'),
]