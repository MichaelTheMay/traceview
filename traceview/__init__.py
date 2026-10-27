"""Traceview — local-first observability for browser agents."""

from traceview.config import load as load_config
from traceview.sdk import instrument
from traceview.storage import init_db

__all__ = ["instrument", "init_db", "load_config"]
__version__ = "0.1.1"
