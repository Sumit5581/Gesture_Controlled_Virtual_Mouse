"""
Configuration file for Virtual Mouse
"""

# Hand Detection Settings
HAND_DETECTION_CONFIDENCE = 0.7
HAND_TRACKING_CONFIDENCE = 0.7
MAX_HANDS = 2

# Gesture Recognition Settings
DISTANCE_THRESHOLD = 30  # Pixels - threshold for finger distance
CLICK_COOLDOWN = 0.3  # Seconds - minimum time between clicks
SCROLL_COOLDOWN = 0.2  # Seconds - minimum time between scrolls

# Scroll Settings
SCROLL_AMOUNT = 3  # Number of scroll units per gesture

# Display Settings
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
SHOW_FPS = True
SHOW_LANDMARKS = True

# Smoothing Settings
CURSOR_SMOOTHING = 0.01  # Duration for smooth cursor movement
