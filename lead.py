"""
Class that contains people who attempt to contact commpany
It consists of name, email, and phone variables,
only one of them need to be non-empty.
"""
class Lead():
    """ all variables can be set to new one, if it's not None value """

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

    def set_name(self, name: str):
        """ set only if value is not None """
        if name is not None:
            self.name = name

    def set_email(self, email: str):
        """ set only if value is not None """
        if email is not None:
            self.email = email

    def set_phone(self, phone: str):
        """ set only if value is not None """
        if phone is not None:
            self.phone = phone

    def to_string(self):
        """
        print string of all variables
        """
        print('Name: {}'.format(self.name))
        print('Email: {}'.format(self.email))
        print('Phone: {}\n'.format(self.phone))
 
        return True
