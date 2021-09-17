"""lunarphases app urls."""
from django.urls import path
from django.utils.translation import gettext as _
from lunarphases.views import (
    CurrentLunarPhaseView,
    FollowingLunarPhasesView,
    MonthlyCalendarView,
    SpecificLunarPhasesView,
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
    ),
    path(
        _('monthly_calendar')+'/<int:year>/<int:month>',
        MonthlyCalendarView.as_view(),
        name='monthly_calendar'
    ),
    path(
         _('projected_phase')+'/<int:year>/<int:month>/<int:day>',
        SpecificLunarPhasesView.as_view(),
        name='specific_lunar_phase'
    )
]
