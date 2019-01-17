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

        context = {
            'lunar_phase': lunar_phase,
            'tips': lunar_phase_tips,
        }

        return HttpResponse(template.render(context, request))
