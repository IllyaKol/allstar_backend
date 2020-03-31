from django.contrib import admin

from .models import Sex
from .models import Club
from .models import Star
from .models import StarUser

admin.site.register(Sex)
admin.site.register(Club)
admin.site.register(Star)
admin.site.register(StarUser)
