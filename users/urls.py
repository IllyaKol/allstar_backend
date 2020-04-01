from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view()),
    path('update/', views.UserRetrieveUpdateAPIView.as_view()),
    path('obtain_token/', views.authenticate_user),
]
