from django.urls import path
from .views import *

urlpatterns = [
    path('auth/', user_login, name="login_auth"),
    path('login/', login_view, name="login_view"),
    path('signup/', signup_view, name="signup_view"),
    path('register/', user_signup, name="user_signup"),
    path('logout/', user_logout, name="logout"),
    # path('profile/', show_profile, name="profile"),
]