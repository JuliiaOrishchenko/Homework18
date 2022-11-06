class Email:
    def __init__(self, name, email):
        self.name = name
        self._email = None
        self.email = email


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if self.validate(email):
            self._email = email
        else:
            raise ValueError("Not valid email")

    @staticmethod
    def validate(email):
        if "@" in email:
            prefix, domain = email.split("@")
            if all(char.isalnum() or char in ".-_" for char in prefix):
                if "." in domain:
                    f_dom, l_dom = domain.split(".")
                    if all(char.isalnum() or char == "-" for char in f_dom):
                        if l_dom.isalnum() and len(l_dom) >= 2:
                            return True
        return False



mail = Email("Olga", "orishchenkoya@gmail.com")
print(mail.__dict__)


