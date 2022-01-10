"""Logger
"""
from configparser import ConfigParser
from importlib import resources

# Log Harvestor's Python Package (log-harvestor-py)
__version__ = "1.0.0"

# Read Config
cfg = ConfigParser()
with resources.path("logger", "config.cfg") as path:
  cfg.read(str(path))

API_URL = cfg.get("logger", "apiUrl")
