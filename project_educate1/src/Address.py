import re

from project_educate1.src.Field import Field
from project_educate1.src.ValidationError import ValidationError


def validate_address(func):
    def wrapper(*args, **kwargs):
        address = args[1]
        if not address.strip():
            raise ValidationError("Address cannot be empty")
        pattern = r"^[a-zA-Z0-9\s.,-]+$"
        if not re.match(pattern, address):
            raise ValidationError("Incorrect address format, please use a valid format")
        return func(*args, **kwargs)

    return wrapper


class Address(Field):
    @validate_address
    def __init__(self, value):
        super().__init__(value)
