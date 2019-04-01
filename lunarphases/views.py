"""lunarphases app views."""
# import os
# import logging
from django.http import (
    HttpResponse,
    # HttpResponseRedirect,
)
from django.template import loader
from django.views import View
from lunarphases import LunarPhase
from .utils import (
    get_lunar_phase_tips,
    get_following_lunar_phases,
)

# logger = logging.getLogger(__name__)


class CurrentLunarPhaseView(View):
    """
    CurrentLunarPhaseView.

    This view represents the current status of the lunar phase.
    """

    def get(self, request):
        template = loader.get_template('index.html')
        lunar_phase = LunarPhase()
        lunar_phase_tips = get_lunar_phase_tips(lunar_phase)
        following_lunar_phases = get_following_lunar_phases(
            following_phases_count=4
        )

        context = {
            'lunar_phase': lunar_phase,
            'tips': lunar_phase_tips,
            'following_lunar_phases': following_lunar_phases,
        }

        return HttpResponse(template.render(context, request))


class FollowingLunarPhasesView(View):
    """
    FollowingLunarPhasesView.

    This view represents the following lunar phases.
    """

    def get(self, request):
        template = loader.get_template('following_lunar_phases.html')
        lunar_phase = LunarPhase()
        # lunar_phase_tips = get_lunar_phase_tips(lunar_phase)
        following_lunar_phases = get_following_lunar_phases(
            following_phases_count=4*4
        )

        context = {
            'lunar_phase': lunar_phase,
            # 'tips': lunar_phase_tips,
            'following_lunar_phases': following_lunar_phases,
        }

        return HttpResponse(template.render(context, request))
