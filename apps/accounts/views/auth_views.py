from apps.accounts.serializers.auth_serializers import UserLoginSerializer, UserRefreshTokenSerializer
from rest_framework import generics, status
from rest_framework.response import Response
# from apps.common.utils import set_response_message

class LoginGenericAPIView(generics.GenericAPIView):
    """
    user Login
    """

    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        response.set_cookie("refresh", str(serializer.data["token"]["refresh"]))
        # set_response_message(self, message="user logined")
        return response


class RefreshGenericAPIView(generics.GenericAPIView):
    """
    refresh token
    """

    serializer_class = UserRefreshTokenSerializer

    def post(self, request):
        data = request.data.copy()
        data["refresh"] = request.COOKIES.get("refresh")
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.get_new_token(serializer.validated_data)
        # set_response_message(self, message="token refreshed")
        return Response(result, status=status.HTTP_200_OK)


class LogoutGenericAPIView(generics.GenericAPIView):
    """
    user logout
    """

    def post(self, request):
        response = Response()
        response.delete_cookie(key="refresh")
        response.data = {}
        response.status = status.HTTP_200_OK
        # set_response_message(self, message="user logouted")
        return response