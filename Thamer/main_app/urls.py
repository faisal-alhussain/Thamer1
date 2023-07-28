from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("company/add/", views.add_company, name="add_company"),
    path("", views.index_page, name="index_page"),
    path("home/about_us/", views.about_us, name="about_us"),
    path("home/ikteva_page/", views.ikteva_page, name="ikteva_page"),
    path("home/market/", views.market_page, name="market_page"),
    path("companys/update/<company_id>/", views.update_company, name="update_company"),
    path("companys/details/<company_id>/", views.company_detail, name="company_detail"),
    path("companys/delete/<company_id>/", views.delete_company, name="delete_company"),
    path("companys/<company_id>/review/add/", views.add_review, name="add_review"),
    path("home/payment/", views.payment_page, name="payment_page"),
    path("home/experts/quastion", views.experts_page, name="experts_page"),
    path("home/companys/", views.company_page, name="company_page"),
    path("companys/owner_details/<company_id>/", views.onwer_details, name="onwer_details"),
    path("sign_up/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path("signout/", views.signout_page, name="signout_page"),



]