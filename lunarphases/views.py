"""lunarphases app views."""
# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class CurrentLunarPhaseView(View):
    """
    CurrentLunarPhaseView.

    This view represents the current status of the lunar phase.
    """

    def get(self, request):
        # <view logic>
        return HttpResponse('Hello moon')
