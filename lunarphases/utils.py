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


def get_lunar_phasename_from_code(code):
    phasenames = {
        'new_moon': _('New Moon'),
        'waxing_crescent': _('Waxing Crescent'),
        'first_quarter': _('First Quarter'),
        'waxing_gibbous': _('Waxing Gibbous'),
        'full_moon': _('Full Moon'),
        'waning_gibbous': _('Waning Gibbous'),
        'last_quarter': _('Last Quarter'),
        'waning_crescent': _('Waning Crescent'),
    }

    return phasenames[code]


def get_lunar_phase_data(now=None):
    astral = Astral()
    moon_phase_day = astral.moon_phase(
        date=now
    )

    phase_code = get_lunar_phasecode_from_day(moon_phase_day)
    phase_name = get_lunar_phasename_from_code(phase_code)

    lunar_phase_data = {
        'datetime': now,
        'code': phase_code,
        'name': phase_name,
        'moon_phase_day': moon_phase_day
    }

    return lunar_phase_data


def get_lunar_phase_tips(lunar_phase):

    PLANT_HARVERST_FLOWER_AND_FRUITS = {
        'title': 'Siembra y cosecha plantas con flores o frutos',
        'message': 'Es recomendable sembrar y cosechar aquellas plantas que cultivamos con el fin de aprovechar sus flores o frutos.'
    }

    PLANT_HARVERST_ROOTS_AND_LEAVES = {
        'title': 'Siembra y cosecha plantas de raices u hojas',
        'message': 'Es recomendable sembrar y cosechar aquellas plantas que cultivamos con el fin de aprovechar sus raices y hojas.'
    }

    HARVEST_FLOWER_AND_FRUITS = {
        'title': 'Cosecha frutos o flores',
        'message': 'Hoy la luna se encuentra en su máxima potencia y toda la savia se concentra en la parte superior de las plantas, por lo tanto es un buen día para cosechar flores o frutos que estén maduros.'
    }

    HARVEST_ROOTS_AND_LEAVES = {
        'title': 'Cosecha raices u hojas',
        'message': 'Hoy toda la savia se concentra en la parte inferior de las plantas, por lo tanto es un buen día para cosechar plantas de raices y hojas.'
    }

    DONT_PRUNE = {
        'title': 'NO realices podas',
        'message': 'No es un buen día para podar tus plantas, debido a que podria suponerles un stress innecesario.',
    }

    CAN_PRUNE = {
        'title': 'Puedes podar tus plantas',
        'message': 'Si podas tus plantas hoy, estas responderán mejor a la poda y les causarás menos stress.',
    }

    CAN_MAKE_CUTTINGS = {
        'title': 'Puedes realizar esquejes',
        'message': 'Si realizas un esqueje hoy, éste tendrá más energia y por lo tanto será más probable que enraice y genere una nueva planta.'
    }

    tips = {
        'new_moon': [
            HARVEST_ROOTS_AND_LEAVES,
        ],
        'waxing_crescent': [
            PLANT_HARVERST_FLOWER_AND_FRUITS,
            DONT_PRUNE,
        ],
        'first_quarter': [
            PLANT_HARVERST_FLOWER_AND_FRUITS,
            DONT_PRUNE,
        ],
        'waxing_gibbous': [
            PLANT_HARVERST_FLOWER_AND_FRUITS,
            DONT_PRUNE,
        ],
        'full_moon': [
            HARVEST_FLOWER_AND_FRUITS,
            CAN_MAKE_CUTTINGS,
        ],
        'waning_gibbous': [
            PLANT_HARVERST_ROOTS_AND_LEAVES,
        ],
        'last_quarter': [
            PLANT_HARVERST_ROOTS_AND_LEAVES,
            CAN_PRUNE,
        ],
        'waning_crescent': [
            PLANT_HARVERST_ROOTS_AND_LEAVES,
            CAN_PRUNE,
        ],
    }

    return tips[lunar_phase.code]
