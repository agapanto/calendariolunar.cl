"""lunarphases app urls."""
from django.urls import path
from lunarphases.views import CurrentLunarPhaseView

urlpatterns = [
    path(
        '',
        CurrentLunarPhaseView.as_view(),
        name='current_lunar_phase'
    )
]
