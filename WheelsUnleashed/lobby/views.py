from django.shortcuts import render

# Create your views here.
def lobbyHome(request):
    return render(request, "lobbyBase.html")