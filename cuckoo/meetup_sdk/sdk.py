import httpx

from datetime import datetime, timedelta

from cuckoo.meetup_sdk import urls


def fetch_group_events(group_id: str, start=None, end=None, params=None):
    url = urls.get_group_events_url(group_id=group_id)
    params = params or {}
    today = datetime.now().date()
    start = start or today
    end = end or today + timedelta(days=6)
    default_params = {
        'no_earlier_than': start.isoformat(),
        'no_later_than': end.isoformat(),
    }
    params = params | default_params
    response = httpx.get(url, params=params)
    events = response.json()
    return events
