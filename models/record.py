"""Module contains Record class representing a contact record."""

from .exceptions import ContactError
from .fields import Name, Phone, Birthday

class Record:
    """
    Represents a contact record with a name and a list of phone numbers.

    Args:
        name (str): The name of the contact.

    Attributes:
        name (Name): The name of the contact.
        phones (list): A list of phone numbers associated with the contact.
        birthday (Birthday): Optional birthday of the contact.
    """

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        """
        Adds a phone number to the contact's list of phone numbers.

        Args:
            phone (Phone): The phone number to add.

        Raises:
            ContactError: If the phone number already exists in the contact's list of phone numbers.
        """
        if self.find_phone(phone):
            raise ContactError("Phone number already exists.")

        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        Removes a phone number from the contact's list of phone numbers.
        Won't raise error if phone number not exist.

        Args:
            phone (str): The phone number to remove.
        """
        existing_phone = self.find_phone(phone)
        if existing_phone:
            self.phones.remove(existing_phone)

    def edit_phone(self, phone: str, new_phone: str):
        """
        Edits a phone number in the contact's list of phone numbers.

        Args:
            phone (str): The phone number to edit.
            new_phone (str): The new phone number.

        Raises:
            ContactError: If the phone number to edit does not exist in the contact's phones list,
                        or if the new phone number already exists in the contact's phones list.
        """
        existing_phone = self.find_phone(phone)
        if not existing_phone:
            raise ContactError("No such phone number.")

        if self.find_phone(new_phone):
            raise ContactError("New phone number already exists.")

        self.phones[self.phones.index(existing_phone)] = Phone(new_phone)

    def find_phone(self, phone: str) -> Phone | None:
        """
        Finds a phone number in the contact's list of phone numbers.

        Args:
            phone (str): The phone number to check.

        Returns:
            Phone: The phone number if found, None otherwise.
        """
        target_phone = Phone(phone)
        return next((p for p in self.phones if p == target_phone), None)

    def add_birthday(self, birthday: str):
        """
        Adds or overrides a birthday of the contact.
        """
        self.birthday = Birthday(birthday)

    def __str__(self):
        chunks = []
        chunks.append(f"Contact name: {self.name}")
        chunks.append(f"phones: {'; '.join(p.value for p in self.phones)}")
        if self.birthday:
            chunks.append(f"birthday: {self.birthday.value.strftime('%d.%m.%Y')}")
        return ", ".join(chunks)
