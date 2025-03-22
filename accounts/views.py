from django.shortcuts import render

# Create your views here.

# accounts/views.py ------------------------------------------------------------------------
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt  # Disable CSRF just for simplicity; consider proper CSRF handling or JWT for production
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)

            # Check if user already exists
            if User.objects(email=email).first():
                return JsonResponse({'error': 'User already exists.'}, status=400)

            # Create new user
            user = User(email=email)
            user.set_password(password)
            user.save()

            return JsonResponse({'message': 'User created successfully!'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



# accounts/views.py ------------------------------------------------------------------------

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

            # If correct, return success
            return JsonResponse({'message': 'Logged in successfully!'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
