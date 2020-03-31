from django.db import models
from django.conf import settings


class Sex(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sex'


class Star(models.Model):
    fullname = models.CharField(max_length=64)
    age = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=255, default=None)
    sex_id = models.ForeignKey(Sex, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'Star'


class StarUser(models.Model):
    star_id = models.ForeignKey(Star, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Star User'
