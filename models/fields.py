"""Module containing the Field class and its subclasses."""

import re
import datetime

class Field:
    """
    Represents a base field object.
    """
    def __init__(self, value: any) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Field):
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

class Name(Field):
    """
    Represents a name field.
    """
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Phone(Field):
    """
    Represents a phone number field.

    Args:
        value (str): The phone number value.

    Attributes:
        value (str): The normalized phone number value.

    Raises:
        ValueError: If the phone number format is not valid.
    """
    pattern = r"[+\d]"
    country_code = "38"

    def __init__(self, value: str) -> None:
        phone = "".join(re.findall(self.pattern, value))

        if not phone.startswith("+"):
            phone = re.sub(fr"^({self.country_code})?", f"+{self.country_code}", phone)

        if len(phone) != 13:
            raise ValueError("Invalid phone number. Use (+38) XXX-XXX-XX-XX format.")

        super().__init__(phone)

class Birthday(Field):
    """
     Represents a birthday field.

     Raises:
        ValueError: If the bitrhday format is not valid.
    """
    def __init__(self, value: str) -> None:
        bday = None
        try:
            bday = datetime.datetime.strptime(value, "%d.%m.%Y")
        except ValueError as e:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from e
        if bday > datetime.datetime.now():
            raise ValueError("Birthday can't be in the future.")
        if bday.year < 1900:
            raise ValueError("Birthday can't be earlier than 1900.")
        super().__init__(bday)
