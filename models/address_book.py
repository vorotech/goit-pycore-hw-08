"""Module containing the AddressBook class."""

import datetime
import pickle

from collections import UserDict

from .exceptions import ContactError
from .fields import Name
from .record import Record

class AddressBook(UserDict):
    """
    A class representing an address book.

    This class extends the UserDict class to provide functionality for managing contacts in an address book.

    Attributes:
        data (dict): A dictionary to store the contacts in the address book.

    Methods:
        add_record(record: Record): Adds a record to the address book.
        find(name: Name) -> Record: Finds a record in the address book by name.
        delete(name: Name): Deletes a record from the address book by name.
    """

    def add_record(self, record: Record) -> None:
        """
        Adds a record to the data dictionary.

        Args:
            record (Record): The record to be added.

        Raises:
            ContactError: If the contact already exists in the data dictionary.
        """
        if record.name in self.data:
            raise ContactError("Contact already exists.")

        self.data[record.name] = record

    def find(self, name: str, raise_error: bool = True) -> Record | None:
        """
        Find a contact by name.

        Args:
            name (str): The name of the contact to find.
            raise_error (bool): Whether to raise an error if the contact is not found.

        Returns:
            Record: The contact record associated with the given name.
            None if not found if raise_error is False.

        Raises:
            ContactError: If no contact with the given name is found. Only if raise_error is True.
        """
        name = Name(name)

        if name not in self.data:
            if raise_error:
                raise ContactError("No such contact.")
            return None

        return self.data[name]

    def delete(self, name: str):
        """
        Deletes the specified name from the data dictionary.
        Won't raise error if phone number not exist.

        Args:
            name (str): The name to be deleted.
        """
        name = Name(name)

        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        """
        Calculates upcoming birthdays of contacts who has their birthday specified
        for next 7 days including today.
        """
        today = datetime.date.today()
        upcoming_birthdays = []

        for user in self.data.values():
            if user.birthday is not None:
                # user.birthday.value is already a datetime.date object
                birthday = user.birthday.value
                birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)
                # 7 days including today is 6 days from today
                if today <= birthday_this_year <= (today + datetime.timedelta(days=6)):
                    congratulation_date = birthday_this_year
                    if birthday_this_year.weekday() in (5, 6):
                        congratulation_date = birthday_this_year + \
                            datetime.timedelta(days = 7 - birthday_this_year.weekday())

                    upcoming_birthdays.append(
                        {
                            'name': user.name.value,
                            'congratulation_date': congratulation_date.strftime("%d.%m.%Y"),
                        }
                    )

        return upcoming_birthdays
