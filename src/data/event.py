from dataclasses import dataclass

from data.dt_off import Repeat
from time_range import TimeRange

@dataclass
class Event:
    title: str
    time: TimeRange
    rep: Repeat
