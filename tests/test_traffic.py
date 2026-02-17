"""
Unit tests for traffic control system
"""

import pytest
from src.traffic_manager import TrafficManager
from src.signal_controller import SignalController


def test_signal_controller():
    """Test signal controller"""
    controller = SignalController("INT_001")
    state = controller.update_signal(60)
    assert state in ["GREEN", "YELLOW", "RED"]


def test_traffic_manager():
    """Test traffic manager"""
    manager = TrafficManager()
    manager.add_intersection("INT_001")
    manager.update_traffic("INT_001", 45, 35.5)
    status = manager.get_system_status()
    assert status["active_intersections"] == 1


def test_data_collection():
    """Test data collection"""
    manager = TrafficManager()
    manager.update_traffic("INT_001", 50, 40.0)
    status = manager.get_system_status()
    assert status["analysis"] is not None 
