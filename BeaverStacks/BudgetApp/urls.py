from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='form'),
    path('add_transaction/', views.add_transaction, name="add_transaction"),
    path('update_transaction/<str:pk>', views.update_transaction, name="update_transaction"),
    path('delete_transaction/<str:pk>', views.delete_transaction, name="delete_transaction"),
]