from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # View to list lost and found items
    path('items/', views.index, name='index'),

    # View to add a lost or found item
    path('add/', views.add_item, name='add_item'),  # Corrected to add_item

    # View to claim a lost or found item (with item_id as a URL parameter)
    path('claim/<int:item_id>/', views.claim_item, name='claim_item'),
]
