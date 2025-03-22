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

