from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import StarUser
from users.views import IsTokenValid
#
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             response = login(request, user)
#             print(response)
#             return redirect('/')
#         else:
#             form = AuthenticationForm()
#             context = {
#                 'form': form,
#                 'tab_name': 'Login',
#                 'user_not_found': 'User Not Found!'
#             }
#             return render(request, 'login.html', context=context)
#     else:
#         if request.user.is_authenticated:
#             return redirect('/')
#         form = AuthenticationForm()
#         context = {
#             'form': form,
#             'tab_name': 'Login'
#         }
#         return render(request, 'login.html', context=context)
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated, IsTokenValid])
# def logout_view(request):
#     logout(request)
#     return redirect('app:login')
#

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def home(request):
    context = {
        'tab_name': 'Home Page'
    }
    return render(request, 'app/home.html', context=context)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsTokenValid])
def get_own_votes(request):
    user_id = request.user.id
    star_ids = [star.id for star in StarUser.objects.filter(user_id=user_id)]
    # return JsonResponse(star_ids)
    return JsonResponse(star_ids, safe=False)


