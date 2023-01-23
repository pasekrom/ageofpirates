from django.db.models.functions import Lower
from django.http import HttpResponse
from django.db import connection
from decimal import Decimal
from django.db.models import F, Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class HomeView(TemplateView):

    template_name = 'ageofpirates/home.html'


class PlayersView(ListView):

    template_name = 'ageofpirates/players.html'

    def get_queryset(self):
        return Player.objects.all().order_by(Lower('jmeno'))

class PlayerView(DetailView):

    template_name = 'ageofpirates/player.html'
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['awards_list'] = Awards.objects.filter(hrac=self.object.id).order_by('-id')
        context['match_list'] = Match.objects.filter(Q(p1=self.object.id) | Q(p2=self.object.id) | Q(p3=self.object.id) | Q(p4=self.object.id) | Q(p5=self.object.id) | Q(p6=self.object.id) | Q(p7=self.object.id) | Q(p8=self.object.id)).order_by('-datum_cas')[:10]
        return context


class MapView(DetailView):

    template_name = 'ageofpirates/map.html'
    model = Map

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['match_list'] = Match.objects.filter(map=self.object.id).order_by('-datum_cas')[:10]
        return context


class CivView(DetailView):

    template_name = 'ageofpirates/civ.html'
    model = Civilization

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MatchesView(ListView):

    template_name = 'ageofpirates/matches.html'

    def get_queryset(self):
        return Match.objects.all().order_by('-datum_cas')[:50]


class MatchView(DetailView):

    template_name = 'ageofpirates/match.html'
    model = Match

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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
        return context


class TournamentsView(ListView):

    template_name = 'ageofpirates/tournaments.html'

    def get_queryset(self):
        return Tournament.objects.all().order_by('-datum_zahajeni')


class nvtpvpflaoe2deView(TemplateView):

    template_name = 'ageofpirates/tournaments/nvtpvpflaoe2de.html'
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class tt3v3View(TemplateView):

    template_name = 'ageofpirates/tournaments/tt3v3.html'
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def kalkulace(request):
    player_list = Player.objects.all()
    match_list = Match.objects.all()
    map_list = Map.objects.all()
    stat_mp = MapPlayerStat.objects.all()
    stat_mc = MapCivStat.objects.all()
    stat_cp = CivPlayerStat.objects.all()
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
            wl = wl*100
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

    return HttpResponse("hotovo")


def test(request):

    player_list = Player.objects.all()
    match_list = Match.objects.all()
    map_list = Map.objects.all()
    civ_list = Civilization.objects.all()
    stat_mp = MapPlayerStat.objects.all()
    stat_mc = MapCivStat.objects.all()
    stat_cp_list = CivPlayerStat.objects.all()
    sql_cpw = ''' --počet her hráče s civkou a výhra
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
        ((p1_id = %s) AND (p1_civ_id = %s) AND (p1_team = win)) OR
        ((p2_id = %s) AND (p2_civ_id = %s) AND (p2_team = win)) OR
        ((p3_id = %s) AND (p3_civ_id = %s) AND (p3_team = win)) OR
        ((p4_id = %s) AND (p4_civ_id = %s) AND (p4_team = win)) OR
        ((p5_id = %s) AND (p5_civ_id = %s) AND (p5_team = win)) OR
        ((p6_id = %s) AND (p6_civ_id = %s) AND (p6_team = win)) OR
        ((p7_id = %s) AND (p7_civ_id = %s) AND (p7_team = win)) OR
        ((p8_id = %s) AND (p8_civ_id = %s) AND (p8_team = win))
    '''

# TODO !!!!!!
    for match in match_list:
        for player in player_list:
            for civ in civ_list:
                with connection.cursor() as cursor:
                    win = cursor.execute(sql_cpw, [player.id, civ.id, player.id, civ.id, player.id, civ.id, player.id, civ.id, player.id, civ.id, player.id, civ.id, player.id, civ.id, player.id, civ.id])
                stat_cp = CivPlayerStat(civ = civ, hrac = player, vyhry = win)
                stat_cp.save()
    ''' počet výher
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_id = xxx) AND (p1_team = win)) OR
    	((p2_id = xxx) AND (p2_team = win)) OR
    	((p3_id = xxx) AND (p3_team = win)) OR
    	((p4_id = xxx) AND (p4_team = win)) OR
    	((p5_id = xxx) AND (p5_team = win)) OR
    	((p6_id = xxx) AND (p6_team = win)) OR
    	((p7_id = xxx) AND (p7_team = win)) OR
    	((p8_id = xxx) AND (p8_team = win))
    '''

    ''' počet proher
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_id = xxx) AND (p1_team != win)) OR
    	((p2_id = xxx) AND (p2_team != win)) OR
    	((p3_id = xxx) AND (p3_team != win)) OR
    	((p4_id = xxx) AND (p4_team != win)) OR
    	((p5_id = xxx) AND (p5_team != win)) OR
    	((p6_id = xxx) AND (p6_team != win)) OR
    	((p7_id = xxx) AND (p7_team != win)) OR
    	((p8_id = xxx) AND (p8_team != win))
    '''

    ''' počet her hráče s civkou a prohra
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_id = 5380164) AND (p1_civ_id = 1) AND (p1_team != win)) OR
    	((p2_id = 5380164) AND (p2_civ_id = 1) AND (p2_team != win)) OR
    	((p3_id = 5380164) AND (p3_civ_id = 1) AND (p3_team != win)) OR
    	((p4_id = 5380164) AND (p4_civ_id = 1) AND (p4_team != win)) OR
    	((p5_id = 5380164) AND (p5_civ_id = 1) AND (p5_team != win)) OR
    	((p6_id = 5380164) AND (p6_civ_id = 1) AND (p6_team != win)) OR
    	((p7_id = 5380164) AND (p7_civ_id = 1) AND (p7_team != win)) OR
    	((p8_id = 5380164) AND (p8_civ_id = 1) AND (p8_team != win))
    '''

    ''' počet her hráče na mapě a výhra
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_id = 5380164) AND (map_id = 3) AND (p1_team = win)) OR
    	((p2_id = 5380164) AND (map_id = 3) AND (p2_team = win)) OR
    	((p3_id = 5380164) AND (map_id = 3) AND (p3_team = win)) OR
    	((p4_id = 5380164) AND (map_id = 3) AND (p4_team = win)) OR
    	((p5_id = 5380164) AND (map_id = 3) AND (p5_team = win)) OR
    	((p6_id = 5380164) AND (map_id = 3) AND (p6_team = win)) OR
    	((p7_id = 5380164) AND (map_id = 3) AND (p7_team = win)) OR
    	((p8_id = 5380164) AND (map_id = 3) AND (p8_team = win))
    '''

    ''' počet her hráče na mapě a prohra
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_id = 5380164) AND (map_id = 3) AND (p1_team != win)) OR
    	((p2_id = 5380164) AND (map_id = 3) AND (p2_team != win)) OR
    	((p3_id = 5380164) AND (map_id = 3) AND (p3_team != win)) OR
    	((p4_id = 5380164) AND (map_id = 3) AND (p4_team != win)) OR
    	((p5_id = 5380164) AND (map_id = 3) AND (p5_team != win)) OR
    	((p6_id = 5380164) AND (map_id = 3) AND (p6_team != win)) OR
    	((p7_id = 5380164) AND (map_id = 3) AND (p7_team != win)) OR
    	((p8_id = 5380164) AND (map_id = 3) AND (p8_team != win))
    '''

    ''' počet her civky na mapě a prohra
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_civ_id != 31) AND (map_id = 3) AND (p1_team != win)) OR
    	((p2_civ_id != 31) AND (map_id = 3) AND (p2_team != win)) OR
    	((p3_civ_id != 31) AND (map_id = 3) AND (p3_team != win)) OR
    	((p4_civ_id != 31) AND (map_id = 3) AND (p4_team != win)) OR
    	((p5_civ_id != 31) AND (map_id = 3) AND (p5_team != win)) OR
    	((p6_civ_id != 31) AND (map_id = 3) AND (p6_team != win)) OR
    	((p7_civ_id != 31) AND (map_id = 3) AND (p7_team != win)) OR
    	((p8_civ_id != 31) AND (map_id = 3) AND (p8_team != win))
    '''

    ''' počet her civky na mapě a výhra
    SELECT COUNT(*)
    FROM ageofpirates_match
    WHERE
    	((p1_civ_id != 31) AND (map_id = 3) AND (p1_team = win)) OR
    	((p2_civ_id != 31) AND (map_id = 3) AND (p2_team = win)) OR
    	((p3_civ_id != 31) AND (map_id = 3) AND (p3_team = win)) OR
    	((p4_civ_id != 31) AND (map_id = 3) AND (p4_team = win)) OR
    	((p5_civ_id != 31) AND (map_id = 3) AND (p5_team = win)) OR
    	((p6_civ_id != 31) AND (map_id = 3) AND (p6_team = win)) OR
    	((p7_civ_id != 31) AND (map_id = 3) AND (p7_team = win)) OR
    	((p8_civ_id != 31) AND (map_id = 3) AND (p8_team = win))
    '''

    return HttpResponse("hotovo")
