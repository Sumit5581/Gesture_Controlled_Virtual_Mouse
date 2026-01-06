import pyautogui
from screeninfo import get_monitors

class MouseController:
    def __init__(self):
        """Initialize mouse controller"""
        # Disable pyautogui failsafe for smoother operation
        pyautogui.FAILSAFE = False
        self.screen_width, self.screen_height = self._get_screen_resolution()
    
    def _get_screen_resolution(self):
        """Get screen resolution"""
        try:
            monitors = get_monitors()
            if monitors:
                primary = monitors[0]
                return primary.width, primary.height
        except:
            pass
        
        # Fallback to pyautogui size
        width, height = pyautogui.size()
        return width, height
    
    def get_screen_size(self):
        """Get screen dimensions"""
        return self.screen_width, self.screen_height
    
    def move_mouse(self, x, y):
        """
        Move mouse cursor to position
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        try:
            # Add some smoothing and bounds checking
            x = max(0, min(x, self.screen_width - 1))
            y = max(0, min(y, self.screen_height - 1))
            pyautogui.moveTo(x, y, duration=0.01)
        except Exception as e:
            print(f"Error moving mouse: {e}")
    
    def left_click(self):
        """Perform left mouse click"""
        try:
            pyautogui.click(button='left')
        except Exception as e:
            print(f"Error performing left click: {e}")
    
    def right_click(self):
        """Perform right mouse click"""
        try:
            pyautogui.click(button='right')
        except Exception as e:
            print(f"Error performing right click: {e}")
    
    def double_click(self):
        """Perform double left click"""
        try:
            pyautogui.doubleClick(button='left')
        except Exception as e:
            print(f"Error performing double click: {e}")
    
    def scroll_up(self, amount=3):
        """
        Scroll up
        
        Args:
            amount: Number of scroll units
        """
        try:
            pyautogui.scroll(amount)
        except Exception as e:
            print(f"Error scrolling up: {e}")
    
    def scroll_down(self, amount=3):
        """
        Scroll down
        
        Args:
            amount: Number of scroll units
        """
        try:
            pyautogui.scroll(-amount)
        except Exception as e:
            print(f"Error scrolling down: {e}")
    
    def drag(self, start_x, start_y, end_x, end_y, duration=0.5):
        """
        Drag mouse from start to end position
        
        Args:
            start_x: Starting X coordinate
            start_y: Starting Y coordinate
            end_x: Ending X coordinate
            end_y: Ending Y coordinate
            duration: Duration of drag action
        """
        try:
            pyautogui.drag(end_x - start_x, end_y - start_y, duration=duration)
        except Exception as e:
            print(f"Error dragging: {e}")
