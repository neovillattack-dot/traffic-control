"""
Configuration settings for traffic control system
"""

# API Configuration
API_ENDPOINT = "https://api.neoville.city/traffic"
API_TIMEOUT = 30

# Traffic Signal Timing (seconds)
GREEN_LIGHT_MIN = 30
GREEN_LIGHT_MAX = 90
YELLOW_LIGHT = 5
RED_LIGHT_MIN = 30

# Monitoring Settings
REFRESH_INTERVAL = 5
MAX_INTERSECTIONS = 200

# Data Processing
BATCH_SIZE = 100
LOG_LEVEL = "INFO"