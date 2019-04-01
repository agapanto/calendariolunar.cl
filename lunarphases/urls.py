"""lunarphases app urls."""
from django.urls import path
from lunarphases.views import (
    CurrentLunarPhaseView,
    FollowingLunarPhasesView,
)

urlpatterns = [
    path(
        '',
        CurrentLunarPhaseView.as_view(),
        name='current_lunar_phase'
    ),
    path(
        'proximas_fases',
        FollowingLunarPhasesView.as_view(),
        name='following_lunar_phases'
    )
]
