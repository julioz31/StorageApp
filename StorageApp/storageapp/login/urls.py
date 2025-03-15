from django.urls import path
from .views import login_view, exit_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', exit_view, name='logout'),
]