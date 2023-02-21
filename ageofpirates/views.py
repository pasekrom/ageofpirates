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
        with connection.cursor() as cursor:
            sql_player_civs = '''
                SELECT 
                    c.id AS civilization_id, 
                    c.nazev AS civilization, 
                    COUNT(*) AS games_played 
                FROM 
                    ageofpirates_player AS p 
                    JOIN ageofpirates_match AS m ON p.id IN (m.p1_id, m.p2_id, m.p3_id, m.p4_id, m.p5_id, m.p6_id, m.p7_id, m.p8_id) 
                    JOIN ageofpirates_civilization AS c ON c.id = CASE p.id
                        WHEN m.p1_id THEN m.p1_civ_id
                        WHEN m.p2_id THEN m.p2_civ_id
                        WHEN m.p3_id THEN m.p3_civ_id
                        WHEN m.p4_id THEN m.p4_civ_id
                        WHEN m.p5_id THEN m.p5_civ_id
                        WHEN m.p6_id THEN m.p6_civ_id
                        WHEN m.p7_id THEN m.p7_civ_id
                        WHEN m.p8_id THEN m.p8_civ_id
                    END
                WHERE 
                    p.id = %s
                GROUP BY 
                    c.id 
                ORDER BY 
                    games_played DESC 
                LIMIT 5;
                '''
            cursor.execute(sql_player_civs, [self.object.id])
            context['player_civs'] = cursor.fetchall()
            sql_player_teammates = '''
                SELECT
                  p2.id AS teammate_id,
                  p2.jmeno AS teammate_name,
                  COUNT(*) AS frequency
                FROM
                  ageofpirates_match m
                  LEFT JOIN ageofpirates_player p1 ON m.p1_id = p1.id
                  LEFT JOIN ageofpirates_player p2 ON m.p2_id = p2.id
                  LEFT JOIN ageofpirates_player p3 ON m.p3_id = p3.id
                  LEFT JOIN ageofpirates_player p4 ON m.p4_id = p4.id
                  LEFT JOIN ageofpirates_player p5 ON m.p5_id = p5.id
                  LEFT JOIN ageofpirates_player p6 ON m.p6_id = p6.id
                  LEFT JOIN ageofpirates_player p7 ON m.p7_id = p7.id
                  LEFT JOIN ageofpirates_player p8 ON m.p8_id = p8.id
                WHERE (p1_id = %s OR
                       p2_id = %s OR
                       p3_id = %s OR
                       p4_id = %s OR
                       p5_id = %s OR
                       p6_id = %s OR
                       p7_id = %s OR
                       p8_id = %s)
                    AND ( 
                  (
                    m.p1_team = m.p2_team AND
                    m.p1_id IS NOT NULL AND m.p2_id IS NOT NULL AND
                    m.p1_id != m.p2_id
                  ) OR (
                    m.p1_team != m.p2_team AND
                    m.p1_id IS NOT NULL AND m.p2_id IS NOT NULL AND
                    m.p1_id != m.p2_id
                  ) OR (
                    m.p1_team = m.p3_team AND
                    m.p1_id IS NOT NULL AND m.p3_id IS NOT NULL AND
                    m.p1_id != m.p3_id
                  ) OR (
                    m.p1_team != m.p3_team AND
                    m.p1_id IS NOT NULL AND m.p3_id IS NOT NULL AND
                    m.p1_id != m.p3_id
                  ) OR (
                    m.p1_team = m.p4_team AND
                    m.p1_id IS NOT NULL AND m.p4_id IS NOT NULL AND
                    m.p1_id != m.p4_id
                  ) OR (
                    m.p1_team != m.p4_team AND
                    m.p1_id IS NOT NULL AND m.p4_id IS NOT NULL AND
                    m.p1_id != m.p4_id
                  ) OR (
                    m.p1_team = m.p5_team AND
                    m.p1_id IS NOT NULL AND m.p5_id IS NOT NULL AND
                    m.p1_id != m.p5_id
                  ) OR (
                    m.p1_team != m.p5_team AND
                    m.p1_id IS NOT NULL AND m.p5_id IS NOT NULL AND
                    m.p1_id != m.p5_id
                  ) OR (
                    m.p1_team = m.p6_team AND
                    m.p1_id IS NOT NULL AND m.p6_id IS NOT NULL AND
                    m.p1_id != m.p6_id
                  ) OR (
                    m.p1_team != m.p6_team AND
                    m.p1_id IS NOT NULL AND m.p6_id IS NOT NULL AND
                    m.p1_id != m.p6_id
                  ) OR (
                    m.p1_team = m.p7_team AND
                    m.p1_id IS NOT NULL AND m.p7_id IS NOT NULL AND
                    m.p1_id != m.p7_id
                  ) OR (
                    m.p1_team != m.p7_team AND
                    m.p1_id IS NOT NULL AND m.p7_id IS NOT NULL AND
                    m.p1_id != m.p7_id
                  ) OR (
                    m.p1_team = m.p8_team AND
                    m.p1_id IS NOT NULL AND m.p8_id IS NOT NULL AND
                    m.p1_id != m.p8_id)
                    )
                GROUP BY
                  p2.id, p2.jmeno
                ORDER BY
                  frequency DESC
                LIMIT 5;
                '''
            cursor.execute(sql_player_teammates, [self.object.id, self.object.id, self.object.id, self.object.id, self.object.id, self.object.id, self.object.id, self.object.id])
            context['player_teammates'] = cursor.fetchall()
            sql_player_enemies = '''
                SELECT 
                    p2.id AS enemy_id, p2.jmeno AS enemy_jmeno, 
                    COUNT(*) AS games_played 
                FROM 
                    ageofpirates_player AS p1 
                    JOIN (
                        SELECT 
                            unnest(array[p1_id, p2_id, p3_id, p4_id, p5_id, p6_id, p7_id, p8_id]) AS player_id, 
                            unnest(array[p1_team, p2_team, p3_team, p4_team, p5_team, p6_team, p7_team, p8_team]) AS p_team, 
                            map_id 
                        FROM 
                            ageofpirates_match
                    ) AS ma1 ON p1.id = ma1.player_id 
                    JOIN (
                        SELECT 
                            unnest(array[p1_id, p2_id, p3_id, p4_id, p5_id, p6_id, p7_id, p8_id]) AS player_id, 
                            unnest(array[p1_team, p2_team, p3_team, p4_team, p5_team, p6_team, p7_team, p8_team]) AS p_team, 
                            map_id 
                        FROM 
                            ageofpirates_match
                    ) AS ma2 ON ma1.map_id = ma2.map_id AND ma1.player_id != ma2.player_id AND ma1.p_team != ma2.p_team 
                    JOIN ageofpirates_player AS p2 ON p2.id = ma2.player_id 
                WHERE 
                    p1.id = %s 
                GROUP BY 
                    p1.id, p2.id 
                ORDER BY 
                    p1.id, games_played DESC 
                LIMIT 5;
                '''
            cursor.execute(sql_player_enemies, [self.object.id])
            context['player_enemies'] = cursor.fetchall()
            sql_player_map = '''
                SELECT 
                    m.nazev AS map_nazev, 
                    COUNT(CASE WHEN ma.win = p_team THEN 1 ELSE NULL END) AS games_won,
                    COUNT(CASE WHEN ma.win = p_team THEN 1 ELSE NULL END) * 100.0 / COUNT(*) AS games_won_percent,
                    COUNT(CASE WHEN ma.win != p_team THEN 1 ELSE NULL END) AS games_lost    
                FROM 
                    ageofpirates_player AS p
                    JOIN (
                        SELECT 
                            unnest(array[p1_id, p2_id, p3_id, p4_id, p5_id, p6_id, p7_id, p8_id]) AS player_id, 
                            unnest(array[p1_team, p2_team, p3_team, p4_team, p5_team, p6_team, p7_team, p8_team]) AS p_team, 
                            win, 
                            map_id 
                        FROM 
                            ageofpirates_match
                    ) AS ma ON p.id = ma.player_id 
                    JOIN ageofpirates_map AS m ON m.id = ma.map_id
                WHERE 
                    p.id = %s
                GROUP BY 
                    p.id, m.id
                ORDER BY 
                    p.id, games_won_percent DESC;
                '''
            cursor.execute(sql_player_map, [self.object.id])
            context['player_map'] = cursor.fetchall()
            sql_player_civ = '''
                            SELECT 
                                c.nazev AS civilization_nazev, 
                                COUNT(CASE WHEN ma.win = ma.p_team THEN 1 ELSE NULL END) AS games_won,
                                ROUND(100.0 * COUNT(CASE WHEN ma.win = ma.p_team THEN 1 ELSE NULL END) / COUNT(*), 2) AS games_won_percent,
                                COUNT(CASE WHEN ma.win != ma.p_team THEN 1 ELSE NULL END) AS games_lost
                            FROM 
                                ageofpirates_player AS p
                                JOIN (
                                    SELECT 
                                        unnest(array[p1_id, p2_id, p3_id, p4_id, p5_id, p6_id, p7_id, p8_id]) AS player_id, 
                                        unnest(array[p1_team, p2_team, p3_team, p4_team, p5_team, p6_team, p7_team, p8_team]) AS p_team, 
                                        unnest(array[p1_civ_id, p2_civ_id, p3_civ_id, p4_civ_id, p5_civ_id, p6_civ_id, p7_civ_id, p8_civ_id]) AS civ_id,
                                        win
                                    FROM 
                                        ageofpirates_match
                                ) AS ma ON p.id = ma.player_id 
                                JOIN ageofpirates_civilization AS c ON c.id = ma.civ_id
                            WHERE 
                                p.id = %s
                            GROUP BY 
                                p.id, c.id
                            ORDER BY 
                                p.id, games_won_percent DESC;
                            '''
            cursor.execute(sql_player_civ, [self.object.id])
            context['player_civ'] = cursor.fetchall()
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

    sql_test = '''
    SELECT p.jmeno AS player_jmeno,
        m.nazev AS civ_name,
        COUNT(*) AS games_played
    FROM ageofpirates_match AS ma
    JOIN ageofpirates_player AS p ON p.id = ma.p1_id OR p.id = ma.p2_id
    JOIN ageofpirates_map AS m ON m.id = ma.map_id
    WHERE p.id IN (SELECT p.id FROM ageofpirates_match)
    GROUP BY p.id, m.id
    ORDER BY p.id, games_played DESC;
    '''

    return HttpResponse("hotovo")


class TestView(TemplateView):

    template_name = 'ageofpirates/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with connection.cursor() as cursor:
            sql_test = '''
                SELECT p.jmeno AS player_jmeno,
                       m.nazev AS map_nazev,
                       COUNT(*) AS games_played
                FROM ageofpirates_match AS ma
                JOIN ageofpirates_player AS p ON p.id = ma.p1_id OR p.id = ma.p2_id OR p.id = ma.p3_id OR p.id = ma.p4_id OR p.id = ma.p5_id OR p.id = ma.p6_id OR p.id = ma.p7_id OR p.id = ma.p8_id
                JOIN ageofpirates_map AS m ON m.id = ma.map_id
                WHERE p.id = %s
                GROUP BY p.id, m.id
                ORDER BY p.id, games_played DESC;
                '''
            cursor.execute(sql_test, [self.request.user.id])
            context['player_map'] = cursor.fetchall()
            sql_test = '''
                SELECT p.jmeno AS player_jmeno,
                       m.nazev AS map_nazev,
                       COUNT(*) AS games_played
                FROM ageofpirates_match AS ma
                JOIN ageofpirates_player AS p ON p.id = ma.p1_id OR p.id = ma.p2_id OR p.id = ma.p3_id OR p.id = ma.p4_id OR p.id = ma.p5_id OR p.id = ma.p6_id OR p.id = ma.p7_id OR p.id = ma.p8_id
                JOIN ageofpirates_map AS m ON m.id = ma.map_id
                WHERE p.id IN (SELECT p.id FROM ageofpirates_match)
                GROUP BY p.id, m.id
                ORDER BY p.id, games_played DESC;
                '''
            cursor.execute(sql_test)
            context['testb'] = cursor.fetchall()
        return context
