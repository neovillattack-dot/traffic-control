"""
Main traffic management module
Coordinates signal control and data processing
"""

import time
from .signal_controller import SignalController
from .data_processor import DataProcessor
from .config import REFRESH_INTERVAL, MAX_INTERSECTIONS


class TrafficManager:
    """Main traffic management system"""
    
    def __init__(self):
        self.intersections = {}
        self.data_processor = DataProcessor()
        self.running = False
    
    def add_intersection(self, intersection_id):
        """Add intersection to monitoring"""
        if intersection_id not in self.intersections:
            self.intersections[intersection_id] = SignalController(intersection_id)
            return True
        return False
    
    def update_traffic(self, intersection_id, vehicle_count, speed):
        """Update traffic data for intersection"""
        if intersection_id not in self.intersections:
            self.add_intersection(intersection_id)
        
        # Update signal
        signal = self.intersections[intersection_id]
        signal.update_signal(vehicle_count)
        
        # Collect data
        self.data_processor.collect_data(intersection_id, vehicle_count, speed)
    
    def get_system_status(self):
        """Get overall system status"""
        status = {
            "active_intersections": len(self.intersections),
            "running": self.running,
            "analysis": self.data_processor.analyze_traffic()
        }
        return status
    
    def start_monitoring(self):
        """Start traffic monitoring"""
        self.running = True
        print(f"Traffic monitoring started for {len(self.intersections)} intersections") 
