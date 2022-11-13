from django.db.models.functions import Lower
from decimal import Decimal
from django.db.models import F
from django.views.generic import TemplateView, ListView, DetailView
from .models import Player, Match, Map, Civilization, Tournament, TournamentMatch


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


class TournamentsMatchesView(ListView):

    template_name = 'ageofpirates/tournaments_matches.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournament'] = Tournament.objects.all()
        return context

    def get_queryset(self):
        return TournamentMatch.objects.all()


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
        player_list = Player.objects.all()
        match_list = Match.objects.all()
        map_list = Map.objects.all()
        match_count = Match.objects.all().count()
        civilization_list = Civilization.objects.all()
        for player in player_list:
            odehrane_hry = Match.objects.filter(p1=player.id).count()
            odehrane_hry += Match.objects.filter(p2=player.id).count()
            odehrane_hry += Match.objects.filter(p3=player.id).count()
            odehrane_hry += Match.objects.filter(p4=player.id).count()
            odehrane_hry += Match.objects.filter(p5=player.id).count()
            odehrane_hry += Match.objects.filter(p6=player.id).count()
            odehrane_hry += Match.objects.filter(p7=player.id).count()
            odehrane_hry += Match.objects.filter(p8=player.id).count()
            vyhry = Match.objects.filter(p1=player.id, p1_team=F('win')).count()
            vyhry += Match.objects.filter(p2=player.id, p2_team=F('win')).count()
            vyhry += Match.objects.filter(p3=player.id, p3_team=F('win')).count()
            vyhry += Match.objects.filter(p4=player.id, p4_team=F('win')).count()
            vyhry += Match.objects.filter(p5=player.id, p5_team=F('win')).count()
            vyhry += Match.objects.filter(p6=player.id, p6_team=F('win')).count()
            vyhry += Match.objects.filter(p7=player.id, p7_team=F('win')).count()
            vyhry += Match.objects.filter(p8=player.id, p8_team=F('win')).count()
            prohry = odehrane_hry - vyhry
            if vyhry != 0:
                wl = round(Decimal(100/(odehrane_hry/vyhry)),2)
            else:
                wl = 0
            wl = Decimal(wl)
            player.odehrane_hry = odehrane_hry
            player.vyhry = vyhry
            player.prohry = prohry
            player.wl = wl
            player.save()
        for map in map_list:
            hry = Match.objects.filter(map=map.id).count()
            if hry != 0:
                hry_proc = round(Decimal(100/(match_count/hry)),2)
            else:
                hry_proc = 0
            map.hry_proc = Decimal(hry_proc)
            map.hry = hry
            map.save()
        for civilization in civilization_list:
            hry = Match.objects.filter(p1_civ=civilization).count()
            hry += Match.objects.filter(p2_civ=civilization).count()
            hry += Match.objects.filter(p3_civ=civilization).count()
            hry += Match.objects.filter(p4_civ=civilization).count()
            hry += Match.objects.filter(p5_civ=civilization).count()
            hry += Match.objects.filter(p6_civ=civilization).count()
            hry += Match.objects.filter(p7_civ=civilization).count()
            hry += Match.objects.filter(p8_civ=civilization).count()
            vyhry = Match.objects.filter(p1_team=F('win'), p1_civ=civilization).count()
            vyhry += Match.objects.filter(p2_team=F('win'), p2_civ=civilization).count()
            vyhry += Match.objects.filter(p3_team=F('win'), p3_civ=civilization).count()
            vyhry += Match.objects.filter(p4_team=F('win'), p4_civ=civilization).count()
            vyhry += Match.objects.filter(p5_team=F('win'), p5_civ=civilization).count()
            vyhry += Match.objects.filter(p6_team=F('win'), p6_civ=civilization).count()
            vyhry += Match.objects.filter(p7_team=F('win'), p7_civ=civilization).count()
            vyhry += Match.objects.filter(p8_team=F('win'), p8_civ=civilization).count()
            civilization.hry = hry
            civilization.vyhry = vyhry
            if hry != 0:
                hry_proc = round(Decimal(100/(match_count/hry)),2)
            else:
                hry_proc = 0
            civilization.hry_proc = Decimal(hry_proc)
            if vyhry != 0:
                vyhry_proc = round(Decimal(100/(match_count/vyhry)),2)
            else:
                vyhry_proc = 0
            civilization.vyhry_proc = Decimal(vyhry_proc)
            civilization.save()
        return context


class TournamentsView(ListView):

    template_name = 'ageofpirates/tournaments.html'

    def get_queryset(self):
        return Tournament.objects.all().order_by('-datum_zahajeni')


class TournamentsDetailView(DetailView):

    template_name = 'ageofpirates/tournaments_detail.html'
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['match_list'] = TournamentMatch.objects.filter(turnaj=1)
        return context
