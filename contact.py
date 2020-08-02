"""
Child class of Lead
Each contacts has name, email, and phone variable.
Name is a must for each contact object.
For phone and email, one of them needs to be non-empty.
"""
from lead import Lead


class Contact(Lead):
    def __init__(self, name: str, email: str = None, phone: int = None):
        self.name = name
        self.email = email
        self.phone = phone


