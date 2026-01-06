# Gesture Controlled Virtual Mouse

A touch-free virtual mouse system that enables users to control mouse cursor and actions using hand gestures captured through a webcam.

## Features

- **Real-time Hand Detection**: Uses MediaPipe to detect hand landmarks in real-time
- **Gesture Recognition**: Recognizes multiple gestures for different mouse actions
- **Cursor Control**: Maps finger positions to screen coordinates for smooth cursor movement
- **Multiple Gestures**:
  - **Left Click**: Index and middle fingers together
  - **Right Click**: Middle and ring fingers together
  - **Scroll Up**: Three fingers together (index, middle, ring)
  - **Scroll Down**: Pinky with other fingers
- **Live Visualization**: See hand landmarks and virtual cursor on the display
- **FPS Display**: Monitor performance in real-time

## Requirements

- Python 3.8 or higher
- Webcam
- Windows, macOS, or Linux

## Installation

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python virtual_mouse.py
```

### Controls

- **Move Cursor**: Move your index finger to control the cursor position
- **Left Click**: Bring your index and middle fingers close together
- **Right Click**: Bring your middle and ring fingers close together
- **Scroll Up**: Extend index, middle, and ring fingers together and move up
- **Scroll Down**: Extend pinky with other fingers
- **Exit**: Press 'q' to quit the application

## How It Works

1. **Hand Detection**: MediaPipe detects hand landmarks (21 key points) in each video frame
2. **Landmark Extraction**: Converts normalized coordinates to pixel coordinates
3. **Gesture Recognition**: Analyzes finger positions and distances to recognize gestures
4. **Mouse Control**: Translates recognized gestures into mouse actions
5. **Real-time Processing**: Processes video frames continuously for smooth operation

## Troubleshooting

### Camera not detected
- Check if your webcam is properly connected
- Ensure no other application is using the camera

### Gestures not recognized
- Make sure your hand is clearly visible in the camera frame
- Adjust lighting for better detection
- Keep your hand within the camera frame

### Mouse movements are jerky
- Ensure good lighting conditions
- Move your hand more smoothly
- Close other applications to free up CPU resources

## Performance Tips

- Better lighting improves hand detection accuracy
- Keep your hand within 2-3 feet of the camera
- Use a high-quality webcam for smoother tracking
- Ensure your computer has adequate processing power

## Gesture Reference

### Index Finger Position
- Controls the mouse cursor
- Move it to move the cursor on screen

### Finger Gestures
- **Index + Middle Together** → Left Click
- **Middle + Ring Together** → Right Click
- **Index + Middle + Ring Together** → Scroll Up
- **Pinky + Other Fingers** → Scroll Down

## Future Enhancements

- Add double-click gesture
- Add drag and drop functionality
- Add keyboard input simulation
- Improve gesture recognition accuracy
- Add gesture calibration
- Support for multiple hands
