from django.db.models.functions import Lower
from django.views.generic import TemplateView, ListView
from .models import Player, Match


class HomeView(TemplateView):

    template_name = 'ageofpirates/home.html'


class PlayersView(ListView):

    template_name = 'ageofpirates/players.html'

    def get_queryset(self):
        return Player.objects.all().order_by(Lower('jmeno'))


class MatchesView(ListView):

    template_name = 'ageofpirates/matches.html'

    def get_queryset(self):
        return Match.objects.all().order_by('-datum_cas')
