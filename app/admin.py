from django.contrib import admin
from django.forms import TextInput

from .models import Sex
from .models import Club
from .models import Star
from .models import StarUser


class StarAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        image_placeholder = 'ronaldinho.png'
        kwargs['widgets'] = {
            'image': TextInput(attrs={'placeholder': image_placeholder})
        }
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        image_name = obj.image.split('/')[-1]
        if not image_name.endswith('.png'):
            image_name = f"{image_name.split('.')[0]}.png"
        obj.image = image_name.lower()
        obj.save()


admin.site.register(Sex)
admin.site.register(Club)
admin.site.register(StarUser)
admin.site.register(Star, StarAdmin)
