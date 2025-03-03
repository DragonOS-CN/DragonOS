"""
Hardware Layer for Robot Control System.
Handles sensor interfaces and hardware drivers.
"""

from .sensor_manager import SensorManager
from .platform_controller import RK358BPlatform
from .driver_interface import DriverSCAN

__all__ = ['SensorManager', 'RKS58BPlatform', 'DriverSCAN'] 