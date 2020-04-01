from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('own_votes/', views.get_own_votes, name='votes'),
]

