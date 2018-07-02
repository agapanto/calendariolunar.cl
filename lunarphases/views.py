"""lunarphases app views."""
import datetime
# import logging
from django.http import (
    HttpResponse,
    # HttpResponseRedirect,
)
from django.template import loader
# from django.urls import reverse
from django.views import View
from lunarphases.utils import get_current_lunar_phase

# logger = logging.getLogger(__name__)


class CurrentLunarPhaseView(View):
    """
    CurrentLunarPhaseView.

    This view represents the current status of the lunar phase.
    """

    def get(self, request):
        template = loader.get_template('index.html')
        now = datetime.datetime.now()
        lunar_phase, distance = get_current_lunar_phase(now)

        context = {
            'now': now,
            'title': 'Hello moon',
            'lunar_phase': lunar_phase,
        }

        return HttpResponse(template.render(context, request))
