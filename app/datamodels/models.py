from moose_lib import Key, moose_data_model
from dataclasses import dataclass
import datetime


@moose_data_model
@dataclass
class UserActivity:
    eventId: Key[str]
    timestamp: str
    userId: str
    activity: str


@moose_data_model
@dataclass
class ParsedActivity:
    eventId: Key[str]
    timestamp: datetime
    userId: str
    activity: str
