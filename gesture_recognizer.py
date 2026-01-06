import numpy as np

class GestureRecognizer:
    def __init__(self, distance_threshold=30):
        self.distance_threshold = distance_threshold
        self.prev_y = 0
    
    def recognize(self, landmarks):
        """
        Recognize hand gestures from landmarks
        
        Args:
            landmarks: List of hand landmarks
            
        Returns:
            gesture: Recognized gesture name
            confidence: Confidence score (0-1)
        """
        if not landmarks or len(landmarks) < 21:
            return None, 0
        
        # Extract key points
        thumb = landmarks[4]
        index = landmarks[8]
        middle = landmarks[12]
        ring = landmarks[16]
        pinky = landmarks[20]
        
        index_pip = landmarks[6]  # Index PIP (middle joint)
        middle_pip = landmarks[10]  # Middle PIP
        ring_pip = landmarks[14]  # Ring PIP
        pinky_pip = landmarks[18]  # Pinky PIP
        
        # Calculate distances
        thumb_index_dist = self._distance(thumb, index)
        index_middle_dist = self._distance(index, middle)
        middle_ring_dist = self._distance(middle, ring)
        ring_pinky_dist = self._distance(ring, pinky)
        
        # Check if fingers are extended (tip below pip)
        index_extended = index[1] > index_pip[1]
        middle_extended = middle[1] > middle_pip[1]
        ring_extended = ring[1] > ring_pip[1]
        pinky_extended = pinky[1] > pinky_pip[1]
        
        # Gesture recognition logic
        
        # Left Click: Index and Middle fingers close together and extended
        if index_extended and middle_extended and index_middle_dist < self.distance_threshold:
            return "left_click", 0.9
        
        # Right Click: Ring and Middle fingers close together and extended
        if middle_extended and ring_extended and middle_ring_dist < self.distance_threshold:
            return "right_click", 0.9
        
        # Scroll Up: Three fingers together (index, middle, ring) moving up
        if index_extended and middle_extended and ring_extended:
            if index_middle_dist < self.distance_threshold and middle_ring_dist < self.distance_threshold:
                return "scroll_up", 0.8
        
        # Scroll Down: Pinky extended with others
        if pinky_extended and index_extended and middle_extended:
            return "scroll_down", 0.8
        
        return None, 0
    
    def _distance(self, point1, point2):
        """Calculate Euclidean distance between two points"""
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
