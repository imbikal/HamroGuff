from django.urls import path
from . import views

urlpatterns = [
    path('', views.hamroguff_list, name='hamroguff_list'),
    path('create/', views.hamroguff_create, name='hamroguff_create'),
    path('<int:hamroguff_id>/edit/', views.hamroguff_edit, name='hamroguff_edit'),
    path('<int:hamroguff_id>/delete/', views.hamroguff_delete, name='hamroguff_delete'),
     path('register/', views.register, name='register'),

]
