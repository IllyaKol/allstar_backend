from django.urls import path
from django.urls import include
from django.contrib import admin


urlpatterns = [
    path('', include('app.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
]
