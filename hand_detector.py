import mediapipe as mp
import cv2
import numpy as np

class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.7, tracking_confidence=0.7):
        """
        Initialize MediaPipe hand detector
        
        Args:
            mode: Static image mode
            max_hands: Maximum number of hands to detect
            detection_confidence: Confidence threshold for hand detection
            tracking_confidence: Confidence threshold for hand tracking
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )
        self.mp_drawing = mp.solutions.drawing_utils
    
    def detect(self, frame):
        """
        Detect hand landmarks in the frame
        
        Args:
            frame: Input video frame
            
        Returns:
            landmarks: List of hand landmarks (normalized coordinates)
            handedness: Hand classification (Left/Right)
        """
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        
        if results.multi_hand_landmarks and results.multi_handedness:
            # Get the first hand detected
            hand_landmarks = results.multi_hand_landmarks[0]
            handedness = results.multi_handedness[0].classification[0].label
            
            # Convert normalized landmarks to pixel coordinates
            h, w, c = frame.shape
            landmarks = []
            for lm in hand_landmarks.landmark:
                x = lm.x * w
                y = lm.y * h
                z = lm.z
                landmarks.append((x, y, z))
            
            return landmarks, handedness
        
        return None, None
    
    def get_distance(self, point1, point2):
        """Calculate Euclidean distance between two points"""
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
