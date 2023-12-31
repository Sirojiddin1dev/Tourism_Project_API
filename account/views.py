from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from main.models import User
from main.serializers import UserSerializer
from .token import get_tokens_for_user


@api_view(['POST'])
def signin_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                tokens = get_tokens_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': tokens,
                }
            else:
                status = 403
                message = "Invalid Password or Username!"
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined! '
            data = {
                'status': status,
                'message': message,
            }

        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def signup_view(request):
    username = request.data.get("username")
    password = request.data.get('password')
    phone_number = request.data.get('phone_number')

    new_user = User.objects.create_user(
        username=username,
        password=password,
        phone_number=phone_number
    )
    serializer = UserSerializer(new_user)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data': 'success'})


class GetUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUser(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUser(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
