import logging

from cuckoo import settings
from cuckoo.scheduler import Scheduler
from cuckoo.service import check_meetup_group_events

logger = logging.getLogger(__file__)


if __name__ == "__main__":
    print("-------------  STARTING cuckoo  ---------------")
    scheduler = Scheduler()
    scheduler.run_every(
        seconds=5,
        action=check_meetup_group_events,
        kwargs={'group_ids': settings.DEFAULT_TARGET_MEETUP_GROUPS}
    )
    import time
    time.sleep(10)
    print("------------ Finished sleeping ---------------")
