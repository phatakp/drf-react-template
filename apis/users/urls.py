from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("token/refresh/", RefreshTokenView.as_view(), name="refresh_token"),
    path("token/logout/", LogoutView.as_view(), name="logout"),
    path("token/", LoginView.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="users_list"),
    path("user/", LoadUserView.as_view(), name="user_detail"),
]
