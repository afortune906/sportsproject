# roster/views.py
from roster.models import Team, Player
from django.shortcuts import render, get_object_or_404

def home(request):
    #return HttpResponse('Hello World!')
    #return render(request, "roster/home.html")
    teams = Team.objects.all()
    context = {
        'teams': teams,
        #'player_count': Player.objects.count(),
        #'team_count': Team.objects.count(),
    }
    return render(request, "roster/home.html", context)

def team(request, pk):
    team = get_object_or_404(Team, id=pk)
    #player = Player.objects.all()
    players = Player.objects.filter(team__pk=pk)
    context = {
        'players': players,
        'team': team,
    }
    return render(request, "roster/team.html", context)
    #team = Team.objects.order_by('?')[0]
    #team = get_object_or_404(Course, id=pk)
    #return render(request, "roster/team.html", {'team': team})

def player(request, pk):
    #player = Player.objects.order_by('?')[0]
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/player.html", {'player': player})