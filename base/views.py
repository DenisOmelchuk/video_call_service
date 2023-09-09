from django.shortcuts import render, redirect, get_object_or_404
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json
from .models import GameRoom, User
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django_registration.backends.activation.views import RegistrationView
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def registerOrLogin(request):
    if request.method == 'POST':
        registration_form = CustomUserCreationForm(request.POST, request.FILES)
        authentication_form = CustomAuthenticationForm(request, data=request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            if user != None:
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Sorry, but something went wrong. Password has to contain 8 symbols (letters&numbers). If your password is correct, then your username is taken, try another one')
        elif authentication_form.is_valid:
            user = authentication_form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        registration_form = CustomUserCreationForm()
        authentication_form = CustomAuthenticationForm()
    context = {
        'registration_form': registration_form,
        'authentication_form' : authentication_form
    }
    return render(request, 'base/register-login.html', context)


def getToken(request):
    # appId & appCertificate were removed due to security reasons
    appId = "..."
    appCertificate = "..."
    channelName = request.GET.get("channel")
    # uid = random.randint(1, 1000)
    uid = request.user.id
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({"token": token, "uid": uid}, safe=False)


def home(request):
    return render(request,'base/home.html')


def lobby(request):
    return render(request, 'base/lobby.html')


def room(request):
    return render(request, 'base/room.html')


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = GameRoom.objects.get_or_create(
        necessary_number_of_players=9,
        room_name=data['room_name']
    )
    member.players.add(request.user.id)
    name = request.user.username
    return JsonResponse({'name': name}, safe=False)




def getMember(request):
    uid = request.GET.get("UID")
    room_name = request.GET.get('room_name')
    user = get_object_or_404(User, id=uid)
    return JsonResponse({"name": user.username}, safe=False)
