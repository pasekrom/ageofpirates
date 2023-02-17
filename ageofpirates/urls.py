from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('kalkulace/', views.kalkulace, name='kalkulace'),
    path('test/', TestView.as_view(), name='test'),
    path('players/', PlayersView.as_view(), name='players'),
    path('player/<pk>', PlayerView.as_view(), name='player'),
    path('map/<pk>', MapView.as_view(), name='map'),
    path('civ/<pk>', CivView.as_view(), name='civ'),
    path('match/<pk>', MatchView.as_view(), name='match'),
    path('games/', MatchesView.as_view(), name='matches'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('tournaments/', TournamentsView.as_view(), name='tournaments'),
    path('tournaments/nvtpvpflaoe2de', nvtpvpflaoe2deView.as_view()),
    path('tournaments/tt3v3', tt3v3View.as_view()),
    path('tournamentsmatch/<pk>', TournamentsMatchesView.as_view(), name='tournamentsmathces'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
