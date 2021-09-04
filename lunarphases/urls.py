"""lunarphases app urls."""
from django.urls import path
from django.utils.translation import gettext as _
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
        _('following_phases'),
        FollowingLunarPhasesView.as_view(),
        name='following_lunar_phases'
    )
]
