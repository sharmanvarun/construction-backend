from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.MaterialList.as_view(), name='material-list'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='material-detail'),
]