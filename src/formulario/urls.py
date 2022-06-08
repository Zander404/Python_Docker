from django.urls import path 
from . import views

urlpatterns = [
   path('',views.home_view, name='home'),

   path('listBanco/', views.BancoList.as_view(), name='listBanco'),
   path('createBanco/', views.BancoCreate.as_view(), name='createBanco'),
   path('updateBanco/<int:pk>/', views.BancoUpdate.as_view(), name='updateBanco'),
   path('deleteBanco/<int:pk>/', views.BancoDelete.as_view(), name='deleteBanco'),


   path('listAgencia/', views.AgenciaList.as_view(), name='listAgencia'),
   path('createAgencia/', views.AgenciaCreate.as_view(), name='createAgencia'),
   path('updateAgencia/<int:pk>/', views.AgenciaUpdate.as_view(), name='updateAgencia'),
   path('deleteAgencia/<int:pk>/', views.AgenciaDelete.as_view(), name='deleteAgencia'),
]


