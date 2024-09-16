import random
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, BaseThrottle


class AnonSustainedThrottle(AnonRateThrottle):
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    scope = "anon_burst"


class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"


# Example of how you could create a custom throttling class
#   override the allow_request() method:
#      return True or False to allow or deny the request
class RandomRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
