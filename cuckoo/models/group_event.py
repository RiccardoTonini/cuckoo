from dataclasses import dataclass

from cuckoo.models.eumerations import MeetupEventStatus


@dataclass
class MeetUpEvent:
    id: str
    group_id: str
    status: MeetupEventStatus
    rsvp_limit: int
    yes_rsvp_count: int
    data: dict
