"""
lunarphases app utils.

----------------------
Code copied from: https://gist.github.com/miklb/ed145757971096565723
the position & phase methods are copied from the link above, and are created
by Sean B. Palmer, from inamidst.com

To the copied code, i have added translations using gettext to display it
correctly on different languages.
"""
import datetime, calendar
from astral.moon import phase
from dateutil.relativedelta import relativedelta
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

    elif day >= 22 and day <= 27:
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


def get_lunar_phase_data(reference_datetime=None, fix_at_noon=True):
    if reference_datetime is None:
        reference_datetime = datetime.datetime.now()

    if fix_at_noon:
        reference_datetime = reference_datetime.replace(
            hour=12,
            minute=0,
            second=0
        )

    moon_phase_day = int(
        phase(date=reference_datetime)
    )

    phase_code = get_lunar_phasecode_from_day(moon_phase_day)
    phase_name = get_lunar_phasename_from_code(phase_code)

    lunar_phase_data = {
        'datetime': reference_datetime,
        'code': phase_code,
        'name': phase_name,
        'moon_phase_day': moon_phase_day
    }

    return lunar_phase_data


def get_lunar_phase_tips(lunar_phase):

    PLANT_HARVERST_FLOWER_AND_FRUITS = {
        'title': _('Sow and harvest plants with flowers or fruits'),
        'message': _('It is advisable to plant and harvest those plants that we grow in order to take advantage of their flowers or fruits.')
    }

    PLANT_HARVERST_ROOTS_AND_LEAVES = {
        'title': _('Sow and harvest root or leaf plants'),
        'message': _('It is advisable to plant and harvest those plants that we grow in order to take advantage of their roots and leaves.')
    }

    HARVEST_FLOWER_AND_FRUITS = {
        'title': _('Harvest fruits or flowers'),
        'message': _('Today the moon is at its maximum power and all the sap is concentrated in the upper part of the plants, therefore it is a good day to harvest flowers or fruits that are ripe.')
    }

    HARVEST_ROOTS_AND_LEAVES = {
        'title': _('Harvest roots or leaves'),
        'message': _('Today all the sap is concentrated in the lower part of the plants, therefore it is a good day to harvest root and leaf plants.')
    }

    DONT_PRUNE = {
        'title': _('DO NOT perform pruning'),
        'message': _('It is not a good day to prune your plants, because it could suppose an unnecessary stress to them.'),
    }

    CAN_PRUNE = {
        'title': _('You can prune your plants'),
        'message': _('If you prune your plants today, they will respond better to pruning and cause less stress.'),
    }

    CAN_MAKE_CUTTINGS = {
        'title': _('You can make cuttings'),
        'message': _('If you make a cutting today, it will have more energy and therefore it will be more likely to root and generate a new plant.')
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


def get_hair_care_tips(lunar_phase):

    DONT_CUT = {
        'title': 'No lo cortes',
        'message': 'En esta fase el cabello está más propenso a caerse debido a que las fibras capilares están debiles.'
    }

    REPAIR_DAMAGE = {
        'title': 'Repara tu cabello',
        'message': 'Aplica un tratamiento si tu cabello se encuentra muy dañado.'
    }

    CUT_HAIR = {
        'title': 'Corta tu cabello',
        'message': 'Si quieres que tu cabello crezca fuerte en poco tiempo, es buen momento para cortarlo.'
    }

    APPLY_TREATMENTS = {
        'title': 'Puedes aplicar tratamientos',
        'message': 'Es buen momento para aplicar tratamientos o tinturas.'
    }

    DONT_CUT_NOW = {
        'title': 'No realices un corte radical',
        'message': 'En esta fase el cabello crece muy rápidamente, por lo cual no es aconsejable realizar un corte radical(cambio de look).'
    }

    CUT_DAMAGED_HAIR = {
        'title': 'Corta el cabello dañado',
        'message': 'Si tu cabello está dañado, hazle un corte para que éste crezca sano, brillante y fuerte.'
    }

    DONT_CUT_SLOW_SPEED = {
        'title': 'No lo cortes',
        'message': 'Si quieres que tu cabello crezca rápido, no es un buen momento para cortarlo.'
    }

    CLEAN = {
        'title': 'Realiza una limpieza',
        'message': 'Haz una limpieza profunda, es etapa de limpieza por lo que no es un buen momento para teñirse.'
    }

    CUT_HAIR_TIPS = {
        'title': 'Corta las puntas',
        'message': 'Es un buen momento si quieres mantener un largo o forma.'
    }

    tips = {
        'new_moon': [
            DONT_CUT,
            REPAIR_DAMAGE,
        ],
        'waxing_crescent': [
            CUT_HAIR,
            APPLY_TREATMENTS,
            DONT_CUT_NOW,
        ],
        'first_quarter': [
            CUT_HAIR,
            APPLY_TREATMENTS,
            DONT_CUT_NOW,
        ],
        'waxing_gibbous': [
            CUT_HAIR,
            APPLY_TREATMENTS,
            DONT_CUT_NOW,
        ],
        'full_moon': [
            CUT_DAMAGED_HAIR,
            DONT_CUT_SLOW_SPEED,
        ],
        'waning_gibbous': [
            CLEAN,
            CUT_HAIR_TIPS
        ],
        'last_quarter': [
            CLEAN,
            CUT_HAIR_TIPS
        ],
        'waning_crescent': [
            CLEAN,
            CUT_HAIR_TIPS
        ],
    }

    return tips[lunar_phase.code]


def get_following_moon_phase_day_delta(current_moon_phase_day):
    following_moon_phase_day_delta = 0

    if current_moon_phase_day % 7 == 0:
        following_moon_phase_day_delta = 1
    else:
        following_moon_phase_day_delta = 7 - (current_moon_phase_day % 7)

    return following_moon_phase_day_delta


def get_following_lunar_phases(reference_datetime=None,
                               following_phases_count=4,
                               fix_at_noon=True):
    following_lunar_phases = []

    if reference_datetime is None:
        reference_datetime = datetime.datetime.now()

    if fix_at_noon:
        reference_datetime = reference_datetime.replace(
            hour=12,
            minute=0,
            second=0
        )

    # Initialize following_datetime with current datetime(reference_datetime)
    following_datetime = reference_datetime
    # Initialize reference_lunar_phase(to compare with following_lunar_phase)
    reference_lunar_phase = get_lunar_phase_data(reference_datetime)

    # for following_phases_counter in range(0, following_phases_count):
    for following_phases_counter in range(0, following_phases_count):
        appended = False

        # While the following lunar phase is not appended
        while appended is False:
            current_lunar_phase = get_lunar_phase_data(following_datetime)

            following_moon_phase_day_delta = get_following_moon_phase_day_delta(
                current_lunar_phase.get('moon_phase_day')
            )

            # Updates following_datetime to the following lunar phase datetime
            following_datetime = following_datetime + relativedelta(
                days=following_moon_phase_day_delta
            )

            # Get following lunar phase
            following_lunar_phase = get_lunar_phase_data(following_datetime)

            # If there are items on following_lunar_phases
            if len(following_lunar_phases) > 0:
                # If the current lunar phase is not the last
                # following_lunar_phases get_lunar_phasecode_from_day item, append it to the array
                if following_lunar_phases[-1].get('code') is not following_lunar_phase.get('code'):
                    following_lunar_phases.append(following_lunar_phase)
                    appended = True

            # If following_lunar_phases is empty
            else:
                if reference_lunar_phase.get('code') is not following_lunar_phase.get('code'):
                    following_lunar_phases.append(following_lunar_phase)
                    appended = True

    return following_lunar_phases


def get_monthly_calendar(reference_datetime=None,
                         fix_at_noon=True):
    monthly_calendar = []

    if reference_datetime is None:
        reference_datetime = datetime.datetime.now()

    if fix_at_noon:
        reference_datetime = reference_datetime.replace(
            day=1,
            hour=12,
            minute=0,
            second=0
        )

    # Initialize following_datetime with current datetime(reference_datetime)
    following_datetime = reference_datetime
    # Initialize reference_lunar_phase(to compare with following_lunar_phase)
    reference_lunar_phase = get_lunar_phase_data(reference_datetime)

    # Get the first day of the month for current year and assign it
    year = reference_datetime.year
    month = reference_datetime.month
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]

    # Add previous days
    for i in reversed(range(1, reference_datetime.isoweekday())):
        past_datetime = reference_datetime - relativedelta(
            days=i
        )

        day = get_lunar_phase_data(past_datetime)
        
        monthly_calendar.append(day)

    # for following_phases_counter in range(0, following_phases_count):
    for following_phases_counter in range(0, len(days)):
        appended = False

        day = get_lunar_phase_data(following_datetime)

        following_datetime = following_datetime + relativedelta(
            days=1
        )

        monthly_calendar.append(day)


    for i in range(monthly_calendar[-1]["datetime"].isoweekday(), 7):
        day = get_lunar_phase_data(following_datetime)
        
        following_datetime = following_datetime + relativedelta(
            days=1
        )
        
        monthly_calendar.append(day)

    return monthly_calendar


def get_limit_datetime(reference_datetime=None,
                       following_phases_count=4,
                       fix_at_00=True):

    if reference_datetime is None:
        reference_datetime = datetime.datetime.now()

    if fix_at_00:
        reference_datetime = reference_datetime.replace(
            day=1,
            hour=0,
            minute=0,
            second=0
        )
    
    minimum_datetime = datetime.datetime(
        year=2018,
        month=1,
        day=1
    )

    limit_datetime = reference_datetime + relativedelta(
        months=7
    ) - relativedelta (
        days=1
    )
    
    return minimum_datetime, limit_datetime
