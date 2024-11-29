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
    path('element/add/', views.add_element, name="element_add"),
    path('element/delete/<int:element_id>/', views.del_element, name="element_del"),
    path('element/edit/<int:element_id>/', views.edit_element, name="element_edit"),
    path('element/<int:element_id>/', views.element, name="element_detail"),
    
]