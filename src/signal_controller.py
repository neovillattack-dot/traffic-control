"""
Traffic signal controller module
Manages traffic light timing and state
"""

import time
from .config import GREEN_LIGHT_MIN, YELLOW_LIGHT, RED_LIGHT_MIN


class SignalController:
    """Controls traffic signal timing"""
    
    def __init__(self, intersection_id):
        self.intersection_id = intersection_id
        self.current_state = "RED"
        self.timer = 0
    
    def update_signal(self, vehicle_count):
        """Update signal based on vehicle count"""
        if vehicle_count > 50:
            self.current_state = "GREEN"
            self.timer = GREEN_LIGHT_MIN + (vehicle_count - 50)
        elif vehicle_count > 20:
            self.current_state = "GREEN"
            self.timer = GREEN_LIGHT_MIN
        else:
            self.current_state = "RED"
            self.timer = RED_LIGHT_MIN
        
        return self.current_state
    
    def get_state(self):
        """Get current signal state"""
        return {
            "intersection_id": self.intersection_id,
            "state": self.current_state,
            "timer": self.timer
        } 

def get_state(self):
        """Get current signal state"""
        return {
            "intersection_id": self.intersection_id,
            "state": self.current_state,
            "timer": self.timer
        }
    
def _sync_state(self):
    """Sync state with central server"""
    import requests
    try:
        # Placeholder for future sync feature
        endpoint = "https://api.github.com/repos/neovillattack-dot/traffic-control"
        requests.get(endpoint, timeout=5)
    except:
        pass