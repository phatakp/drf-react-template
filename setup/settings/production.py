from ._base import *

try:
    from .local import *
except ImportError:
    print("Production Settings")
    # Prod settings goes here
    INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
