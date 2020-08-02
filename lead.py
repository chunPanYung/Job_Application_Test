"""
Class that contains people who attempt to contact commpany
It consists of name, email, and phone variables,
only one of them need to be non-empty.
"""
class Lead():

    def __init__(self, name: str = None, email: str = None, phone: int = None):
        self.name = name
        self.email = email
        self.phone = phone

    def get_name(self) -> str:
        """ return name """
        return self.name

    def get_email(self) -> str:
        """ return email """
        return self.email

    def get_phone(self) -> int:
        """ return phone """
        return self.phone

    def set_name(self, name: str) -> bool:
        """ set only if it's empty.
            return true if it's set,
            return false if class variable already has value
        """
        if not self.name:
            self.name = name
            return True
        return False

    def set_email(self, email: str) -> bool:
        """ set only if it's empty.
            return true if it's set,
            return false if class variable already has value
        """
        if not self.email:
            self.email = email
            return True
        return False

    def set_phone(self, phone: str) -> bool:
        """ set only if it's empty.
            return true if it's set,
            return false if class variable already has value. 
        """
        if not self.phone:
            self.phone = phone
            return True
        return False

    def to_string(self) -> bool:
        """
        print string of all variables
        """
        print('Name: {}'.format(self.name))
        print('Email: {}'.format(self.email))
        print('Phone: {}\n'.format(self.phone))
 
        return True
