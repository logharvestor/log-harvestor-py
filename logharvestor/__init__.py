"""Log-Harvestor-Py"""
from configparser import ConfigParser
from importlib import resources

# Read Config
cfg = ConfigParser()
with resources.path("logharvestor", "config.cfg") as path:
  cfg.read(str(path))

API_URL = cfg.get("forwarder", "apiUrl")

from logharvestor.forwarder import Forwarder
