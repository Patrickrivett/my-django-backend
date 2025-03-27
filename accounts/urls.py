from django.urls import path
from .views import signup
from .views import login_view
from .views import protected_endpoint
from .views import profile_view
from .views import MongoTokenObtainPairView
from .views import search_ingredients
from .views import search_problems


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile_view'),
    path('protected/', protected_endpoint, name='protected_endpoint'),
    path('token/', MongoTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('ingredients/search/', search_ingredients, name='search_ingredients'),
    path('problems/search/', search_problems, name='search_problems'),
]