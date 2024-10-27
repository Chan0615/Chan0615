from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_expenses, name='list_expenses'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
]