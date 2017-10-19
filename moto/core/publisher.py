

class EventTypes(object):
    RDS2_DATABASE_CREATED = 10
    RDS2_DATABASE_MODIFIED = 20
    RDS2_EVENT_SUBSCRIPTION_CREATED = 30
    RDS2_SNAPSHOT_CREATED = 40
    RDS2_DATABASE_DELETED = 50


class Publisher(object):
    events = EventTypes

    def __init__(self):
        self.reset()

    def subscribe(self, observer, *event_types):
        for event_type in event_types:
            self._observers.setdefault(event_type, []).append(observer)

    def notify(self, event_type, data):
        for observer in self._observers.get(event_type, []):
            observer(event_type, data)

    def reset(self):
        self._observers = {}


default_publisher = Publisher()
