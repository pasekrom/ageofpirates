from django.db import models


class Player(models.Model):
    id = models.BigIntegerField(primary_key=True)
    jmeno = models.TextField()
    img = models.TextField()
    statistika = models.TextField()
    steam = models.TextField()

    class Meta:
        verbose_name = 'Hráč'
        verbose_name_plural = 'Hráči'

    def __str__(self):
        return f'{self.jmeno}'


class Civilization(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.TextField()
    emblem = models.ImageField(upload_to='emblems/')

    class Meta:
        verbose_name = 'Civilizace'
        verbose_name_plural = 'Civilizace'

    def __str__(self):
        return f'{self.nazev}'


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    nazev = models.TextField()
    img = models.ImageField(upload_to='maps/')

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapy'

    def __str__(self):
        return f'{self.nazev}'


class Match(models.Model):
    id = models.BigIntegerField(primary_key=True)
    datum_cas = models.DateTimeField(blank=True, null=True)
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
