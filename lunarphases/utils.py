"""
lunarphases app utils.

----------------------
Code copied from: https://gist.github.com/miklb/ed145757971096565723
the position & phase methods are copied from the link above, and are created
by Sean B. Palmer, from inamidst.com

To the copied code, i have added translations using gettext to display it
correctly on different languages.
"""
import datetime
import decimal
import math
from django.utils.translation import gettext as _

dec = decimal.Decimal


def position(now=None):
    """Get the current moon position."""
    if now is None:
        now = datetime.datetime.now()

    diff = now - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)


def phase(pos):
    """Get the current moon phase."""
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return {
      0: _("New Moon"),
      1: _("Waxing Crescent"),
      2: _("First Quarter"),
      3: _("Waxing Gibbous"),
      4: _("Full Moon"),
      5: _("Waning Gibbous"),
      6: _("Last Quarter"),
      7: _("Waning Crescent")
    }[int(index) & 7]


def get_current_lunar_phase():
    pos = position()
    phasename = phase(pos)

    roundedpos = round(float(pos), 3)

    return phasename, roundedpos
