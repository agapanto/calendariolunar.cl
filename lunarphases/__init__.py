"""lunarphases."""
from .utils import (
    get_current_lunar_phase_data,
)


class LunarPhase:
    """
    LunarPhase class.

    The LunarPhase class allows to easily instantiate *n* lunar phases given a
    datetime, if none is provided, the used datetime will be
    datetime.datetime.now()
    """

    def __init__(self, datetime=None):
        """
        Initialize the current Lunar Phase instance.

        When datetime is None, get_current_lunar_phase_data will use
        datetime.datetime.now() automatically.
        """
        lunar_phase_data = get_current_lunar_phase_data(datetime)

        self.datetime = datetime
        self.name = lunar_phase_data[0]
        self.position = lunar_phase_data[1]
        self.rounded_position = lunar_phase_data[2]
