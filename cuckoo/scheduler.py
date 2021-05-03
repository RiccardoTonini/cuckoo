import functools
import logging
import sched
import threading


logger = logging.getLogger(__file__)


class Scheduler(threading.Thread):
    def __init__(self, start=True):
        self._scheduler = sched.scheduler()
        self._running = True
        super().__init__(daemon=True)
        if start:
            self.start()

    def stop(self):
       self._running = False

    def run(self):
        while self._running:
            delta = self._scheduler.run(blocking=False)
            delta = 0.5 if delta is None else delta
            self._scheduler.delayfunc(min(delta, 0.5))

    def run_at(self, time, action, priority=0, args=None, kwargs=None) -> sched.Event:
        return self._scheduler.enterabs(
            time=time,
            priority=priority,
            action=action,
            argument=args or tuple(),
            kwargs=kwargs or {},
        )

    def run_after(self, delay, action, priority=0, args=None, kwargs=None) -> sched.Event:
        return self._scheduler.enter(
            delay=delay,
            priority=priority,
            action=action,
            argument=args or tuple(),
            kwargs=kwargs or {},
        )

    def run_every(self, seconds, action, args=None, kwargs=None):
        @functools.wraps(action)
        def _wrapped_action(*args, **kwargs):
            try:
                logger.info(f"----------- Scheduler running action {action.__name__} -----------------")
                return action(*args, **kwargs)
            finally:
                return self.run_after(seconds, _wrapped_action, args=args, kwargs=kwargs)

        return self.run_after(seconds, _wrapped_action, args=args, kwargs=kwargs)
