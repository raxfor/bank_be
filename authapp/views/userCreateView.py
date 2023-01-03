from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authapp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "username": request.data["username"],
            "password": request.data["password"]
        }
        tokeSerializer = TokenObtainPairSerializer(data=tokenData)
        tokeSerializer.is_valid(raise_exception=True)

        return Response(tokeSerializer.validated_data, status=status.HTTP_201_CREATED)