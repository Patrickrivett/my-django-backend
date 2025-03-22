from django.urls import path
from .views import signup
from .views import login_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]