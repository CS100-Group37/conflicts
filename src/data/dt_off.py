from dataclasses import dataclass
from enum import Enum
import json

class RepType(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    YEARLY = 4

    def to_string(self):
        match self:
            case RepType.DAILY: return "d"
            case RepType.WEEKLY: return "w"
            case RepType.MONTHLY: return "m"
            case RepType.YEARLY: return "y"

    @classmethod
    def from_string(cls, s) -> RepType:
        match s:
            case "d": return cls.DAILY
            case "w": return cls.WEEKLY
            case "m": return cls.MONTHLY
            case "y": return cls.YEARLY
            #TODO: put a proper error in
            case _: raise

@dataclass
class Repeat:
    num: int
    typ: RepType

    def to_json(self):
        d = self.__dict__
        d["typ"] =  d["typ"].to_string()
        return json.dumps(d)

    @classmethod
    def from_json(cls, s):
        j = json.loads(s)
        if "num" not in j or "typ" not in j: 
            return None
        return Repeat(**{
            "num": j["num"],
            "typ": RepType.from_string(j["typ"])
        })
        

    @classmethod
    def from_string(cls, s):
        p = 0
        
        num = int(s[1:-1])
        typ = RepType.from_string(s[-1])

        return cls(num, typ)

