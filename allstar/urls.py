from django.urls import path
from django.urls import include
from django.contrib import admin

from .utils import update_token_cache
from .connection import init_connections

urlpatterns = [
    path('', include('app.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
]

redis_connection = init_connections()
token_cache = update_token_cache()
