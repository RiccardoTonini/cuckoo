import logging

from cuckoo import settings
from cuckoo.meetup_sdk import sdk
from cuckoo.models.eumerations import MeetupEventStatus
from cuckoo import notifications

logger = logging.getLogger(__file__)


def is_upcoming_event(event) -> bool:
    return event['status'] == MeetupEventStatus.UPCOMING.value


def is_event_almost_full(event, threshold=settings.DEFAULT_TARGET_EVENT_RSVP_THRESHOLD) -> bool:
    yes_rsvp_count = int(event['yes_rsvp_count'])
    rsvp_limit = int(event['rsvp_limit'])
    free_rsvps = rsvp_limit - yes_rsvp_count
    return 0 < free_rsvps <= threshold


def is_target_event(event) -> bool:
    return is_upcoming_event(event) and is_event_almost_full(event)


def get_target_events(events):
    logger.info(f"------- Checking events for MeetUp group {group_id} ---------")
    events = sdk.fetch_group_events(group_id=group_id)

    return [event for event in events if is_target_event(event)]


def check_meetup_group_events(group_ids=settings.DEFAULT_TARGET_MEETUP_GROUPS):
    target_events = []
    for group_id in group_ids:
        events = sdk.fetch_group_events(group_id=group_id)
        print(f"------------------- Fetched events {len(events)} --------------------")
        target_events.extend(get_target_events(events))

    notifications.send_alarm(target_events)
