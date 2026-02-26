"""
KPI Dashboard Package
A Spark-based KPI Dashboard for processing and visualizing key performance indicators
"""

__version__ = "1.0.0"
__author__ = "KPI Dashboard Team"

from .kpi_processor import KPIProcessor
from .dashboard import Dashboard

__all__ = ['KPIProcessor', 'Dashboard']
