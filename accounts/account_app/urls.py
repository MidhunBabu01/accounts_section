from django.urls import path
from account_app import views


app_name="account_app"

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
]
