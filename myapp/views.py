from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserDetails
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

@csrf_exempt
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
 
    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# @login_required
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to the login page
    # return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

# @login_required
@api_view(['POST'])
def save_user(request):
    print(request.user)
    print(request.user.is_authenticated)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User information saved successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def is_logged_in(request):
    """
    Check if the user is logged in.
    """
    if request.user.is_authenticated:
        return Response({'isLoggedIn': True}, status=status.HTTP_200_OK)
    else:
        return Response({'isLoggedIn': False}, status=status.HTTP_200_OK)
