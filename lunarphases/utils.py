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

    if day == 0:
        phasename = _('New Moon')

    elif day >= 1 and day < 7:
        phasename = _('Waxing Crescent')

    elif day == 7:
        phasename = _('First Quarter')

    elif day >= 8 and day < 14:
        phasename = _('Waxing Gibbous')

    elif day == 14:
        phasename = _('Full Moon')

    elif day >= 15 and day < 21:
        phasename = _('Waning Gibbous')

    elif day == 21:
        phasename = _('Last Quarter')

    elif day >= 22 and day < 27:
        phasename = _('Waning Crescent')

    else:
        pass

    return phasename


def get_lunar_phasecode_from_day(day):
    phase_code = ''

    if day == 0:
        phase_code = 'new_moon'

    elif day >= 1 and day < 7:
        phase_code = 'waxing_crescent'

    elif day == 7:
        phase_code = 'first_quarter'

    elif day >= 8 and day < 14:
        phase_code = 'waxing_gibbous'

    elif day == 14:
        phase_code = 'full_moon'

    elif day >= 15 and day < 21:
        phase_code = 'waning_gibbous'

    elif day == 21:
        phase_code = 'last_quarter'

    elif day >= 22 and day < 27:
        phase_code = 'waning_crescent'

    else:
        pass

    return phase_code


def get_lunar_phase_data(now=None):
    astral = Astral()
    moon_phase_day = astral.moon_phase(
        date=now
    )

    phase_name = get_lunar_phasename_from_day(moon_phase_day)
    phase_code = get_lunar_phasecode_from_day(moon_phase_day)

    lunar_phase_data = {
        'datetime': now,
        'code': phase_code,
        'name': phase_name,
        'moon_phase_day': moon_phase_day
    }

    return lunar_phase_data
