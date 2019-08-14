from django.urls import path
from .views import login, signup, dashboard, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
]
