class MailList():
    """docstring for Maillist"""
    def __init__(self, name, ):
        self.__name = name
        self.__contacts = {}

    @property
    def contacts(self):
        return self.__contacts

    @contacts.setter
    def contacts(self, value):
        self.__contacts = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_contact(self, name, email):
        self.__contacts[name] = email

    def update_contact(self, name, email):
        self.__contacts[name] = email

    def remove_contact(self, name):
        del self.__contacts[name]

    def has_contact(self, name):
        return name in self.__contacts

    def has_email(self, email):
        for key in self.__contacts:
            if self.__contacts[key] == email:
                return True
        return False

    
