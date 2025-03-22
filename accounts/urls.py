from django.urls import path
from .views import signup
from .views import login_view
from .views import protected_endpoint

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('protected/', protected_endpoint, name='protected_endpoint'),

]