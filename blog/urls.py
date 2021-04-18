from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
  #  path('post/grilla', views.post_grilla, name='post_grilla'),
    
    path('show',views.show),
    #base de datos clientes
    #path('clientes/display'),views.display,name='display'),
    ]