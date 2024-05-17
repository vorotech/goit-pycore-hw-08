"""Module containing custom exceptions."""

class ContactError(Exception):
    """Custom exception for contact errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
