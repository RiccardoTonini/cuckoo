import logging

logger = logging.getLogger(__file__)


def send_alarm(target_events):
    msg = f"----------  send_alarm for {len(target_events)} target events --------------"
    print(msg)
    logger.info(msg)

    if not target_events:
        return

    # @TODO send sms notification
