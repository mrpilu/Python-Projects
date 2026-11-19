from django.urls import path

from . import views

urlpatterns = [
    # Home page: index.html
    path('', views.home, name='index'),
    # Create New Account page: CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # Balance Sheet page: BalanceSheet.html (/balance/ alone shows an empty sheet,
    # /<id>/balance/ shows one account)
    path('balance/', views.balance, name='balance'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    # Add New Transaction page: AddTransaction.html
    path('transaction/', views.transaction, name='transaction'),
]
