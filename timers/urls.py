from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'timers', views.TimerViewSet, basename='Timer')

urlpatterns = [
    path('', include(router.urls)),
    path('timerstarts', views.TimerStartView.as_view(), name='TimerStart'),
    path('timerstops', views.TimerStopView.as_view(), name='TimerStop')
]
