from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/<int:collec_id>', views.collection, name="collec_detail"),
    path('all/', views.collectionList, name='collec_list'),
    path('new/', views.new_collec, name="collec_new"),
    path('delete/<int:collec_id>', views.del_collec, name="collec_del"),
    path('change/<int:collec_id>/', views.change_collec, name="collec_change"),
    
]