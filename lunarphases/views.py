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

# logger = logging.getLogger(__name__)


class CurrentLunarPhaseView(View):
    """
    CurrentLunarPhaseView.

    This view represents the current status of the lunar phase.
    """

    def get(self, request):
        template = loader.get_template('index.html')
        lunar_phase = LunarPhase()

        context = {
            'now': lunar_phase.datetime,
            'title': 'Hello moon',
            'lunar_phase': lunar_phase.name,
        }

        return HttpResponse(template.render(context, request))
