"""forwarder
"""
from configparser import ConfigParser
from importlib import resources


# Log Harvestor's Python Package (log-harvestor-py)
__version__ = "0.0.6"

# Read Config
cfg = ConfigParser()
with resources.path("logharvestor", "config.cfg") as path:
  cfg.read(str(path))

API_URL = cfg.get("forwarder", "apiUrl")

from logharvestor.forwarder import Forwarder
