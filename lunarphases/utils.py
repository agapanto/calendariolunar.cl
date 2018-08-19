"""
lunarphases app utils.

----------------------
Code copied from: https://gist.github.com/miklb/ed145757971096565723
the position & phase methods are copied from the link above, and are created
by Sean B. Palmer, from inamidst.com

To the copied code, i have added translations using gettext to display it
correctly on different languages.
"""
# import datetime
from astral import Astral
from django.utils.translation import gettext as _


def get_lunar_phasename_from_day(day):
    phasename = ''

    if day >= 0 and day < 7:
        phasename = _('New Moon')

    elif day >= 7 and day < 14:
        phasename = _('First Quarter')

    elif day >= 14 and day < 21:
        phasename = _('Full Moon')

    else:
        phasename = _('Last Quarter')

    return phasename


def get_lunar_phase_data(now=None):
    astral = Astral()
    moon_phase_day = astral.moon_phase(
        date=now
    )

    phase_name = get_lunar_phasename_from_day(moon_phase_day)
    phase_code = phase_name.lower().replace(' ', '_')

    lunar_phase_data = {
        'datetime': now,
        'code': phase_code,
        'name': phase_name,
        'moon_phase_day': moon_phase_day
    }

    return lunar_phase_data
