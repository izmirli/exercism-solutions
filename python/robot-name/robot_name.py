"""Robot Name."""
import random
from string import digits, ascii_uppercase as uc_letters


class Robot:
    """Robot settings and functions."""
    assignd_names = set()
    
    def __init__(self):
        self.name = None
        self.set_name()

    def reset(self):
        """Reset robot to its factory settings."""
        self.name = None
        self.set_name()
        

    def set_name(self):
        """Set unique random name."""
        while self.name is None or self.name in Robot.assignd_names:
            self.name = ''.join(random.choices(uc_letters, k=2) + random.choices(digits, k=3))
        Robot.assignd_names.add(self.name)        
