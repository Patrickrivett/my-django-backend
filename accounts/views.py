from django.shortcuts import render

# Create your views here.

# accounts/views.py ------------------------------------------------------------------------
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@csrf_exempt  # Disable CSRF just for simplicity; consider proper CSRF handling or JWT for production
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')
            name = data.get('name')
            age_group = data.get('age_group')
            hair_types = data.get('hair_types', [])  # array of strings
            skin_types = data.get('skin_types', [])
            allergies = data.get('allergies', [])

            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)

            # Check if user already exists
            if User.objects(email=email).first():
                return JsonResponse({'error': 'User already exists.'}, status=400)

            # Create new user
            user = User(
                email=email,
                name=name,
                age_group=age_group,
                hair_types=hair_types,
                skin_types=skin_types,
                allergies=allergies
            )
            user.set_password(password)
            user.save()

            # Generate JWT tokens for the user
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'User created successfully!',
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



# login view, allows user to login by comparing input to users in database --------------------------------------------



@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Email and password required.'}, status=400)

            # Find user by email
            user = User.objects(email=email).first()
            if not user:
                return JsonResponse({'error': 'User does not exist.'}, status=400)

            # Check password
            if not user.check_password(password):
                return JsonResponse({'error': 'Incorrect password.'}, status=400)

            # Generate JWT tokens for the user
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'Logged in successfully!',
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


# uploading and editing profile screen to cater to what user is online --------------------------------------------



@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user  # JWTAuthentication sets this automatically
    if request.method == 'GET':
        return Response({
            'name': user.name,
            'age_group': user.age_group,
            'hair_types': user.hair_types,
            'skin_types': user.skin_types,
            'allergies': user.allergies,
        })
    elif request.method == 'PUT':
        data = request.data
        user.name = data.get('name', '')
        user.age_group = data.get('age_group', '')
        user.hair_types = data.get('hair_types', [])
        user.skin_types = data.get('skin_types', [])
        user.allergies = data.get('allergies', [])
        user.save()
        return Response({'message': 'Profile updated successfully!'})

    
    # protected JWT endpoint --------------------------------------------

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    # request.user is set by the JWTAuthentication class
    return Response({
        'message': f'Hello, {request.user.email}! This is protected data.',
        'user_id': str(request.user.id)
    })

    # serializer --------------------------------------------
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MongoTokenObtainPairSerializer

class MongoTokenObtainPairView(TokenObtainPairView):
    serializer_class = MongoTokenObtainPairSerializer

# views.py

from .models import Ingredient
from .serializers import IngredientSerializer

@api_view(['GET'])
def search_ingredients(request):
    # Get the query from the URL: /ingredients/search?q=something
    query = request.GET.get('q', '')
    if not query:
        return Response({'error': 'No search query provided'}, status=400)
    
    # Perform a simple case-insensitive search on the name field:
    # e.g., name__icontains=query
    # You could also search by tags, description, etc.
    ingredients = Ingredient.objects(name__icontains=query)

    # Serialize the results
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

from .serializers import ProblemSerializer
from .models import Problem

@api_view(['GET'])
def search_problems(request):
    # Get the query from the URL: /ingredients/search?q=something
    query = request.GET.get('q', '')
    if not query:
        return Response({'error': 'No search query provided'}, status=400)
    
    # Perform a simple case-insensitive search on the name field:
    # e.g., name__icontains=query
    # You could also search by tags, description, etc.
    problems = Problem.objects(name__icontains=query)

    # Serialize the results
    serializer = ProblemSerializer(problems, many=True)
    return Response(serializer.data)
