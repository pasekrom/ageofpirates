from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    PlayersView,
    MatchesView,
    StatsView,
    TournamentsView,
    TournamentsDetailView,
    TournamentsMatchesView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('players/', PlayersView.as_view(), name='players'),
    path('games/', MatchesView.as_view(), name='matches'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('tournaments/', TournamentsView.as_view(), name='tournaments'),
    path('tournaments/<pk>', TournamentsDetailView.as_view()),
    path('tournamentsmatch/<pk>', TournamentsMatchesView.as_view(), name='tournamentsmathces'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
