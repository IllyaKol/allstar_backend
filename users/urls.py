from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.authenticate_user),
    path('logout/', views.logout),
    path('create/', views.CreateUserAPIView.as_view()),
    path('update/', views.UserRetrieveUpdateAPIView.as_view()),
]
