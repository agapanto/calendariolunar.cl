"""lunarphases app views."""
# import os
# import logging
import datetime
from django.http import (
    HttpResponse,
    # HttpResponseRedirect,
)
from django.template import loader
from django.views import View
from dateutil.relativedelta import relativedelta
from lunarphases import LunarPhase
from .utils import (
    get_lunar_phase_tips,
    get_hair_care_tips,
    get_following_lunar_phases,
    get_monthly_calendar,
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
        hair_care_tips = get_hair_care_tips(lunar_phase)
        following_lunar_phases = get_following_lunar_phases(
            following_phases_count=4
        )

        context = {
            'lunar_phase': lunar_phase,
            'tips': lunar_phase_tips,
            'hair_tips': hair_care_tips,
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
        todays_lunar_phase = LunarPhase()
        # lunar_phase_tips = get_lunar_phase_tips(lunar_phase)
        following_lunar_phases = get_following_lunar_phases(
            following_phases_count=4*4
        )

        context = {
            'todays_lunar_phase': todays_lunar_phase,
            # 'tips': lunar_phase_tips,
            'following_lunar_phases': following_lunar_phases,
        }

        return HttpResponse(template.render(context, request))


class MonthlyCalendarView(View):
    """
    MonthlyCalendarView.

    This view represents a Monthly Calendar.
    """

    def get(self, request, year, month):
        template = loader.get_template('monthly_calendar.html')
        reference_datetime = datetime.datetime(
            year=year,
            month=month,
            day=1
        )
        previous_month_datetime = reference_datetime - relativedelta(
            months=1
        )
        following_month_datetime = reference_datetime + relativedelta(
            months=1
        )

        todays_lunar_phase = LunarPhase()
        following_lunar_phases = get_monthly_calendar(
            reference_datetime=reference_datetime
        )

        context = {
            'reference_datetime': reference_datetime,
            'previous_month_datetime': previous_month_datetime,
            'following_month_datetime': following_month_datetime,
            'todays_lunar_phase': todays_lunar_phase,
            'following_lunar_phases': following_lunar_phases,
        }

        return HttpResponse(template.render(context, request))


class SpecificLunarPhasesView(View):
    """
    SpecificLunarPhasesView.

    This view represents the lunar phases on a certain date.
    """

    def get(self, request, year, month, day):
        template = loader.get_template('specific.html')

        reference_datetime = datetime.datetime(
            year=year,
            month=month,
            day=day
        )

        todays_lunar_phase = LunarPhase()
        lunar_phase = LunarPhase(reference_datetime=reference_datetime)
        lunar_phase_tips = get_lunar_phase_tips(lunar_phase)
        hair_care_tips = get_hair_care_tips(lunar_phase)
        # following_lunar_phases = get_following_lunar_phases(
        #     following_phases_count=4
        # )

        context = {
            'todays_lunar_phase': todays_lunar_phase,
            'lunar_phase': lunar_phase,
            'tips': lunar_phase_tips,
            'hair_tips': hair_care_tips,
            # 'following_lunar_phases': following_lunar_phases,
        }

        return HttpResponse(template.render(context, request))
