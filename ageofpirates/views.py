from django.db.models.functions import Lower
from django.views.generic import TemplateView, ListView, DetailView
from .models import Player, Match, Map, Civilization, Tournament


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


class StatsView(ListView):

    template_name = 'ageofpirates/stats.html'

    def get_queryset(self):
        return Player.objects.all().order_by(Lower('jmeno'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_list'] = Player.objects.all()
        context['map_list'] = Map.objects.all()
        context['civilization_list'] = Civilization.objects.all()
        context['match_list'] = Match.objects.all()

        return context


class TournamentsView(ListView):

    template_name = 'ageofpirates/tournaments.html'

    def get_queryset(self):
        return Tournament.objects.all().order_by('-datum_zahajeni')


class TournamentsDetailView(DetailView):

    template_name = 'ageofpirates/tournaments_detail.html'
    model = Tournament
