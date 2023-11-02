from decouple import config

if config('DEBUG', cast=bool):
    from .development import *
else:
    from .production import *
