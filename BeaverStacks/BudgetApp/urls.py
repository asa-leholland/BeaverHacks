from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='form'),
    path('', views.add_transaction, name="add_transaction"),
]