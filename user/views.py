from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import RegistrationSerializer, ProfileSerializer


class RegistrationView(APIView):
    @classmethod
    def post(cls, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            activation_url = request.build_absolute_uri(reverse('activate-account', args=[user.pk, token]))
            send_mail(
                subject="Activate Your Account",
                message=f"Activate your account here: {activation_url}",
                from_email="palitra@gmail.com",
                recipient_list=[user.email],
            )
            return Response({"message": "User created. Activation email sent."}, status=200)
        return Response(serializer.errors, status=400)


class ActivateAccountView(APIView):
    @classmethod
    def get(cls, request, user_id, token):
        try:
            user = User.objects.get(pk=user_id)
            if default_token_generator.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"message": "Account activated successfully!"}, status=200)
            return Response({"error": "Invalid token."}, status=400)
        except User.DoesNotExist:
            return Response({"error": "Invalid user."}, status=400)


class PasswordResetView(APIView):
    @classmethod
    def post(cls, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = request.build_absolute_uri(reverse('password-reset-confirm', args=[user.pk, token]))
            send_mail(
                subject="Password Reset",
                message=f"Reset your password here: {reset_url}",
                from_email="palitra@gmail.com",
                recipient_list=[user.email],
            )
            return Response({"message": "Password reset email sent."}, status=200)
        except User.DoesNotExist:
            return Response({"error": "Invalid email address."}, status=400)


class PasswordResetConfirmView(APIView):
    @classmethod
    def post(cls, request, user_id, token):
        try:
            user = User.objects.get(pk=user_id)
            if PasswordResetTokenGenerator().check_token(user, token):
                new_password = request.data.get('password')
                user.set_password(new_password)
                user.save()
                return Response({"message": "Password reset successful."}, status=200)
            return Response({"error": "Invalid token."}, status=400)
        except User.DoesNotExist:
            return Response({"error": "Invalid user."}, status=404)


class PasswordUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @classmethod
    def post(cls, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        if not user.check_password(current_password):
            return Response({"error": "Current password is incorrect."}, status=400)
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password updated successfully."}, status=200)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @classmethod
    def get(cls, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

    @classmethod
    def put(cls, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

