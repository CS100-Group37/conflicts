from dataclasses import dataclass
import json


@dataclass
class TimeRange:
    """
    A range in time, represented as the range between two time vals, each of an hour and a minute, stored internally in 12 hour format.
    """
    start_h: int
    start_m: int

    end_h: int
    end_m: int

    @staticmethod
    def parse_segment(s):
        pm = False

        s = s.strip()

        if s[-1].lower() in "ap":
            pm = s[-1].lower() == "p"
            s = s[:-1]

        if ":" in s:
            h, m = s.split(":")
            h = int(h.strip())
            m = int(m.strip())
            if pm: h += 12
            return (h,m)
        else:
            h = int(s)
            if pm: h += 12
            return (h, 0)

    @classmethod
    def from_json(cls, s):
        return cls(**json.loads(s))

    @classmethod
    def from_str(cls, s):
        start, end = s.split("-")
        
        start_h, start_m = TimeRange.parse_segment(start)
        end_h, end_m = TimeRange.parse_segment(end)

        return cls(start_h, start_m, end_h, end_m)

    def to_str(self):
        return f"{self.start_h}:{self.start_m:02} - {self.end_h}:{self.end_m:02}"

    def to_json(self):
        return json.dumps(self.__dict__)
