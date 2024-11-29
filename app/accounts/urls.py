from django.urls import path

from . import views

# app_name = "accounts"

urlpatterns = [
    path("", views.account_list, name="account-list"),
    path("account-create/", views.add_account_view, name="account-create"),
    path("account-detail/<slug:slug>/", views.account_detail_view, name="account-detail"),
    path("account-update/<slug:slug>/", views.account_update_view, name="account-update"),
]
