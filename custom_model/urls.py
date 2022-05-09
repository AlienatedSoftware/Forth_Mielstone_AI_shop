from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='custom_model'),
    path('nft/<int:nft_id>', views.nft_by_id, name='nft_by_id'),
]