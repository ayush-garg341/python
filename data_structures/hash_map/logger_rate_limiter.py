"""
For the given stream of message requests and their timestamps as input,
you must implement a logger rate limiter system that decides whether the
current message request is displayed.

The decision depends on whether the same message has already been displayed
in the last S seconds.
"""


class RequestLogger:
    def __init__(self, time_limit):
        # Initialize your data structure here
        self.time_limit = time_limit
        self.request_hash_map = {}

    def message_request_decision(self, timestamp, request):
        if request not in self.request_hash_map:
            self.request_hash_map[request] = timestamp
            return True
        old_timestamp = self.request_hash_map[request]
        if timestamp - old_timestamp >= self.time_limit:
            self.request_hash_map[request] = timestamp
            return True
        return False
