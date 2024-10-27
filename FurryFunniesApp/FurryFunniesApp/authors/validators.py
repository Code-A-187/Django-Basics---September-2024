from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:

    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value):
        if not value.isalpha():
            return ValidationError(self.message)


@deconstructible
class SixDigitsValidator:

    def __init__(self, password=None):
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if value is None:
            self.__password = "Your passcode must be exactly 6 digits!"
        else:
            self.__password = value

    def __call__(self, value):
        if not (value.isdigit() and len(value) == 6):
            return ValidationError(self.password)