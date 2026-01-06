import cv2
import mediapipe as mp
import numpy as np
from hand_detector import HandDetector
from gesture_recognizer import GestureRecognizer
from mouse_controller import MouseController
import time

class VirtualMouseApp:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.hand_detector = HandDetector()
        self.gesture_recognizer = GestureRecognizer()
        self.mouse_controller = MouseController()
        
        # Get screen dimensions
        self.screen_width, self.screen_height = self.mouse_controller.get_screen_size()
        
        # Video frame dimensions
        self.frame_width = 1280
        self.frame_height = 720
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        
        # FPS and timing
        self.ptime = 0
        self.ctime = 0
        self.click_cooldown = 0
        self.scroll_cooldown = 0
        
    def run(self):
        print("Virtual Mouse Started!")
        print("Press 'q' to quit")
        print("=" * 50)
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Flip frame for selfie view
            frame = cv2.flip(frame, 1)
            
            # Detect hand landmarks
            hand_landmarks, handedness = self.hand_detector.detect(frame)
            
            if hand_landmarks:
                # Get gesture from hand landmarks
                gesture, confidence = self.gesture_recognizer.recognize(hand_landmarks)
                
                # Get index and middle finger tips for cursor control
                index_finger = hand_landmarks[8]  # Index finger tip
                middle_finger = hand_landmarks[12]  # Middle finger tip
                ring_finger = hand_landmarks[16]  # Ring finger tip
                pinky_finger = hand_landmarks[20]  # Pinky finger tip
                thumb = hand_landmarks[4]  # Thumb tip
                
                # Map finger position to screen
                x = int(np.interp(index_finger[0], (0, self.frame_width), (0, self.screen_width)))
                y = int(np.interp(index_finger[1], (0, self.frame_height), (0, self.screen_height)))
                
                # Move mouse cursor
                self.mouse_controller.move_mouse(x, y)
                
                # Handle gestures with cooldown
                current_time = time.time()
                
                # Left click - Index and middle fingers down
                if gesture == "left_click" and (current_time - self.click_cooldown) > 0.3:
                    self.mouse_controller.left_click()
                    self.click_cooldown = current_time
                    print("Left Click")
                
                # Right click - Ring and middle fingers down
                elif gesture == "right_click" and (current_time - self.click_cooldown) > 0.3:
                    self.mouse_controller.right_click()
                    self.click_cooldown = current_time
                    print("Right Click")
                
                # Scroll up - Fingers moving upward
                elif gesture == "scroll_up" and (current_time - self.scroll_cooldown) > 0.2:
                    self.mouse_controller.scroll_up()
                    self.scroll_cooldown = current_time
                
                # Scroll down - Fingers moving downward
                elif gesture == "scroll_down" and (current_time - self.scroll_cooldown) > 0.2:
                    self.mouse_controller.scroll_down()
                    self.scroll_cooldown = current_time
                
                # Draw hand landmarks on frame
                self._draw_landmarks(frame, hand_landmarks, handedness)
                self._draw_cursor(frame, index_finger)
            
            # Display FPS
            self.ctime = time.time()
            fps = 1 / (self.ctime - self.ptime) if (self.ctime - self.ptime) > 0 else 0
            self.ptime = self.ctime
            
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Press 'q' to quit", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Display frame
            cv2.imshow("Virtual Mouse - Gesture Controlled", frame)
            
            # Quit on 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cleanup()
    
    def _draw_landmarks(self, frame, landmarks, handedness):
        """Draw hand landmarks on the frame"""
        h, w, c = frame.shape
        
        # Draw circles for each landmark
        for i, landmark in enumerate(landmarks):
            x, y = int(landmark[0]), int(landmark[1])
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        # Draw connections between landmarks
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),  # Thumb
            (0, 5), (5, 6), (6, 7), (7, 8),  # Index
            (0, 9), (9, 10), (10, 11), (11, 12),  # Middle
            (0, 13), (13, 14), (14, 15), (15, 16),  # Ring
            (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky
        ]
        
        for start, end in connections:
            x1, y1 = int(landmarks[start][0]), int(landmarks[start][1])
            x2, y2 = int(landmarks[end][0]), int(landmarks[end][1])
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    def _draw_cursor(self, frame, index_finger):
        """Draw virtual cursor on the frame"""
        x, y = int(index_finger[0]), int(index_finger[1])
        cv2.circle(frame, (x, y), 15, (0, 255, 255), 2)
        cv2.circle(frame, (x, y), 5, (0, 255, 255), -1)
    
    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        print("Virtual Mouse closed.")

if __name__ == "__main__":
    app = VirtualMouseApp()
    app.run()
