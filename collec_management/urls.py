from django.urls import path

from . import views

app_name = 'collec_management'

urlpatterns = [
    path('', views.index, name='index'),
    path('collection/<int:id>/', views.detailCollection, name='detailCollection'),
    path('all/', views.list, name='all'),
    path('new/', views.CreateCollection, name='new'),
    path('delete/<int:id>/', views.deleteCollection, name='delete'),
    path('change/<int:id>/', views.changeCollection, name='change'),
]