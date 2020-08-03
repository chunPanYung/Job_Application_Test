"""
Child class of Lead
Each contacts has name, email, and phone variable.
Name is a must for each contact object.
For phone and email, one of them needs to be non-empty.

Non-empty values in Contacts should not be updated
"""
from lead import Lead


class Contact(Lead):
    """ class Contact, inherited from Lead class, with new restriction:
        such as Name is a must have, and non-empty values in Contacts
        should not be updated
    """

    def __init__(self, name: str, email: str = None, phone: int = None):
        self.name = name
        self.email = email
        self.phone = phone

    def set_name(self, name: str):
        """ set only if it's empty.
            return true if it's set,
            return false if class variable already has value
        """
        if not self.name:
            self.name = name
            return True
        return False

    def set_email(self, email: str):
        """ set only if it's empty.
            return true if it's set,
            return false if class variable already has value
        """
        if not self.email:
            self.email = email
            return True
        return False

    def set_phone(self, phone: str):
        """ set only if it's empty.
            return true if it's set,
            return false if class variable already has value. 
        """
        if not self.phone:
            self.phone = phone
            return True
        return False
