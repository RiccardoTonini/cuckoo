from urllib.parse import urlencode

from cuckoo.meetup_sdk import settings


def get_base_url() -> str:
    return f"{settings.PROTOCOL}://{settings.HOST_NAME}"


def get_group_events_url(group_id: str) -> str:
    base_url = get_base_url()
    return f"{base_url}/{group_id}/events"


def get_group_event_url(event_id: str) -> str:
    base_url = get_base_url()
    return f"{base_url}/events/{event_id}"
