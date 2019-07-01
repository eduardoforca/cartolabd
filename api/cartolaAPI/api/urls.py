from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

router.register('userClub',UserClubModelViewSet)
router.register('realClub',RealClubModelViewSet)
router.register('position',PositionModelViewSet)
router.register('player',PlayerModelViewSet)
router.register('round',RoundModelViewSet)
router.register('match',MatchModelViewSet)
router.register('formation',FormationModelViewSet)
router.register('stat',StatModelViewSet)
router.register('league',LeagueModelViewSet)
router.register('fmupos',FMTPosModelViewSet)
router.register('playerStats',PlayerStatsModelViewSet)
router.register('squad',SquadModelViewSet)
router.register('selected',SelectedModelViewSet)
router.register('clubLeague',ClubLeagueModelViewSet)
router.register('playerPrice',PlayerPriceModelViewSet)

urlpatterns = [
    path('', include((router.urls, 'api'))),
]