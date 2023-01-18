from django.db import models


class Player(models.Model):
    id = models.BigIntegerField(primary_key=True)
    jmeno = models.TextField()
    img = models.TextField()
    statistika = models.TextField()
    steam = models.TextField()
    odehrane_hry = models.BigIntegerField(blank=True, null=True)
    vyhry = models.BigIntegerField(blank=True, null=True)
    prohry = models.BigIntegerField(blank=True, null=True)
    wl = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7)

    class Meta:
        verbose_name = 'Hráč'
        verbose_name_plural = 'Hráči'

    def __str__(self):
        return f'{self.jmeno}'


class Civilization(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.TextField()
    emblem = models.ImageField(upload_to='emblems/')
    hry = models.BigIntegerField(blank=True, null=True)
    vyhry = models.BigIntegerField(blank=True, null=True)
    hry_proc = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    vyhry_proc = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Civilizace'
        verbose_name_plural = 'Civilizace'

    def __str__(self):
        return f'{self.nazev}'


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.TextField()
    img = models.ImageField(upload_to='maps/')
    hry = models.BigIntegerField(blank=True, null=True)
    hry_proc = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    prum_doba = models.TimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapy'

    def __str__(self):
        return f'{self.nazev}'


class Match(models.Model):
    id = models.BigIntegerField(primary_key=True)
    datum_cas = models.DateTimeField(blank=True, null=True)
    delka_hry = models.TimeField(blank=True, null=True)
    pocet_hracu = models.PositiveSmallIntegerField()
    pocet_tymu = models.PositiveSmallIntegerField(blank=True, null=True)
    p1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player1')
    p1_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player1_civ')
    p1_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player2')
    p2_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player2_civ')
    p2_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p3 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player3')
    p3_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player3_civ')
    p3_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p4 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player4')
    p4_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player4_civ')
    p4_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p5 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player5')
    p5_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player5_civ')
    p5_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p6 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player6')
    p6_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player6_civ')
    p6_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p7 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player7')
    p7_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player7_civ')
    p7_team = models.PositiveSmallIntegerField(blank=True, null=True)
    p8 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player8')
    p8_civ = models.ForeignKey(Civilization, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'player8_civ')
    p8_team = models.PositiveSmallIntegerField(blank=True, null=True)
    win = models.PositiveSmallIntegerField()
    map = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Hra'
        verbose_name_plural = 'Hry'

    def __str__(self):
        return f'{self.id}'


class PlayerStat(models.Model):
    hrac = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    hry = models.BigIntegerField(blank=True, null=True)
    vyhry = models.BigIntegerField(blank=True, null=True)
    prohry = models.BigIntegerField(blank=True, null=True)
    rank = models.BigIntegerField(blank=True, null=True)
    elo = models.BigIntegerField(blank=True, null=True)


class MapPlayerStat(models.Model):
    map = models.ForeignKey(Map, null=True, on_delete=models.SET_NULL)
    hrac = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    vyhry = models.BigIntegerField(blank=True, null=True)
    prohry = models.BigIntegerField(blank=True, null=True)


class MapCivStat(models.Model):
    map = models.ForeignKey(Map, null=True, on_delete=models.SET_NULL)
    civ = models.ForeignKey(Civilization, null=True, on_delete=models.SET_NULL)
    vyhry = models.BigIntegerField(blank=True, null=True)
    prohry = models.BigIntegerField(blank=True, null=True)


class CivPlayerStat(models.Model):
    civ = models.ForeignKey(Civilization, null=True, on_delete=models.SET_NULL)
    hrac = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    vyhry = models.BigIntegerField(blank=True, null=True)
    prohry = models.BigIntegerField(blank=True, null=True)


class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.TextField()
    datum_zahajeni = models.DateTimeField(blank=True, null=True)
    pocet_hracu = models.PositiveSmallIntegerField(blank=True, null=True)
    vitez = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL)
    info = models.TextField(blank=True)
    info_ef = models.TextField(blank=True)
    info_qf = models.TextField(blank=True)
    info_sf = models.TextField(blank=True)
    info_f = models.TextField(blank=True)
    p1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer1')
    p2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer2')
    p3 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer3')
    p4 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer4')
    p5 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer5')
    p6 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer6')
    p7 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer7')
    p8 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer8')
    p9 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer9')
    p10 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer10')
    p11 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer11')
    p12 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer12')
    p13 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer13')
    p14 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer14')
    p15 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer15')
    p16 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'tplayer16')
    qfa1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer1')
    qfa2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer2')
    qfb1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer3')
    qfb2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer4')
    qfc1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer5')
    qfc2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer6')
    qfd1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer7')
    qfd2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'qplayer8')
    sfa1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'splayer1')
    sfa2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'splayer2')
    sfb1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'splayer3')
    sfb2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'splayer4')
    f1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'fplayer1')
    f2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'fplayer2')
    fb1 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'bplayer1')
    fb2 = models.ForeignKey(Player, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'bplayer2')
    p1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p3_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p4_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p5_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p6_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p7_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p8_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p9_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p10_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p11_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p12_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p13_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p14_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p15_score = models.PositiveSmallIntegerField(blank=True, null=True)
    p16_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfa1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfa2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfb1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfb2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfc1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfc2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfd1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    qfd2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    sfa1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    sfa2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    sfb1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    sfb2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    f1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    f2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    fb1_score = models.PositiveSmallIntegerField(blank=True, null=True)
    fb2_score = models.PositiveSmallIntegerField(blank=True, null=True)
    map1 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map1')
    map2 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map2')
    map3 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map3')
    map4 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map4')
    map5 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map5')
    map6 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map6')
    map7 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map7')
    map8 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map8')
    map9 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map9')
    map10 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map10')
    map11 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map11')
    map12 = models.ForeignKey(Map, blank=True, null=True, on_delete=models.SET_NULL, related_name = 'map12')

    class Meta:
        verbose_name = 'Turnaj'
        verbose_name_plural = 'Turnaje'

    def __str__(self):
        return f'{self.nazev}'


class TournamentMatch(models.Model):
    turnaj = models.ForeignKey(Tournament, blank=True, null=True, on_delete=models.SET_NULL)
    hra = models.ForeignKey(Match, blank=True, null=True, on_delete=models.SET_NULL)
    ef1 = models.BooleanField(default=False)
    ef2 = models.BooleanField(default=False)
    ef3 = models.BooleanField(default=False)
    ef4 = models.BooleanField(default=False)
    ef5 = models.BooleanField(default=False)
    ef6 = models.BooleanField(default=False)
    ef7 = models.BooleanField(default=False)
    ef8 = models.BooleanField(default=False)
    qf1 = models.BooleanField(default=False)
    qf2 = models.BooleanField(default=False)
    qf3 = models.BooleanField(default=False)
    qf4 = models.BooleanField(default=False)
    sf1 = models.BooleanField(default=False)
    sf2 = models.BooleanField(default=False)
    f = models.BooleanField(default=False)
    fb = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Turnajová hra'
        verbose_name_plural = 'Turnajové hry'

    def __str__(self):
        return f'{self.turnaj} - {self.hra}'


class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    hrac = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    umisteni = models.PositiveSmallIntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Ocenění'
        verbose_name_plural = 'Ocenění'

    def __str__(self):
        return f'{self.hrac} - {self.umisteni} {self.text}'
