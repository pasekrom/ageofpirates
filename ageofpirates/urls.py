from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    PlayersView,
    MatchesView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('players/', PlayersView.as_view(), name='players'),
    path('games/', MatchesView.as_view(), name='matches'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
