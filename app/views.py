from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Star
from .models import StarUser
from users.views import IsTokenValid


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def stars(request):
    context = {
        'tab_name': 'Home Page'
    }
    return render(request, 'app/home.html', context=context)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def get_starts_data(request):
    response = []
    for star in Star.objects.all():
        stars_info = dict()
        stars_info['id'] = star.id
        stars_info['fullname'] = star.fullname
        stars_info['age'] = star.age
        stars_info['description'] = star.description
        stars_info['image'] = None
        stars_info['sex'] = star.sex_id.name
        stars_info['votes'] = StarUser.objects.filter(star_id=star.id).count()
        response.append(stars_info)
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def voting(request, star_id):
    try:
        StarUser.objects.get(star_id=star_id, user_id=request.user.id).delete()
        response = {'status': 'DELETE'}
        return Response(response, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        try:
            StarUser(
                star_id=Star.objects.get(id=star_id),
                user_id=request.user
            ).save()
            response = {'status': 'ADD'}
            return Response(response, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            response = {'status': 'NOT_FOUND'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
