from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.stars, name='starts'),
    path('data/', views.get_starts_data, name='stars_data'),
    path('voting/<int:star_id>', views.voting, name='voting'),
]
