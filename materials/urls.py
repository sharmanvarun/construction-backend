from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.MaterialList.as_view(), name='material-list'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='material-detail'),
    path('materials/<int:pk>/update_amount/', views.MaterialUpdateAmount.as_view(), name='material-update-amount'),

]