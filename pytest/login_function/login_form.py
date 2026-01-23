import re
from typing import Dict, List

class LoginForm:
    """Login form with simple email and password validation."""
    
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 128
    
    def __init__(self):
        self.errors: List[str] = []
        
    def validate_email(self, email: str) -> bool:
        if not email:
            self.errors.append("Email is required.")
            return False 
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            self.errors.append("Invalid email format.")
            return False 
        
        return True 
    
    def validate_password(self, password: str) -> bool: 
        if not password:
            self.errors.append("Password is required")
            return False 