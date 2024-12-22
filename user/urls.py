from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, ActivateAccountView, PasswordResetView, PasswordUpdateView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('activate/<int:user_id>/<str:token>/', ActivateAccountView.as_view(), name='activate-account'),
    path('reset/', PasswordResetView.as_view(), name='password_reset'),
    path('reset/<int:user_id>/<str:token>/', PasswordResetView.as_view(), name='password-reset-confirm'),
    path('update/', PasswordUpdateView.as_view(), name='password_update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
