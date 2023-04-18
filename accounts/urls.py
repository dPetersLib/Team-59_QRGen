from django.urls import path
from .views import Register, Login, logoutuser, adminReg
app_name = "accounts"


urlpatterns = [
    path('register/', Register, name="register-page"),
    path('register/admin/', adminReg, name="adminreg"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name="logout" )
]