"""lunarphases."""
import datetime
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

    def __init__(self, reference_datetime=None):
        """
        Initialize the current Lunar Phase instance.

        When datetime is None, datetime.datetime.now() will be used.
        """
        if reference_datetime is None:
            reference_datetime = datetime.datetime.now()

        lunar_phase_data = get_current_lunar_phase_data(
            reference_datetime
        )

        self.datetime = reference_datetime
        self.name = lunar_phase_data[0]
        self.position = lunar_phase_data[1]
        self.rounded_position = lunar_phase_data[2]
