"""Main module."""

import handler
import pickle

from models import AddressBook

def parse_input(user_input: str) -> tuple:
    """Parses user input and returns command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def save_data(book: AddressBook, filename="addressbook.pkl"):
    """Saves the address book to a file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Loads the address book from a file."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    """Main function."""
    print("Welcome to the assistant bot!")

    # attempt to load the address book from file
    book = load_data()

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            print(handler.get_all_contacts(args, book))

        elif command == "add":
            print(handler.add_contact(args, book))

        elif command == "change":
            print(handler.change_contact(args, book))

        elif command == "contact":
            print(handler.get_contact(args, book))

        elif command == "delete":
            print(handler.delete_contact(args, book))

        elif command == "add-birthday":
            print(handler.add_birthday(args, book))

        elif command == "show-birthday":
            print(handler.show_birthday(args, book))

        elif command == "birthdays":
            print(handler.birthdays(args, book))

        else:
            print("Invalid command. Usage: hello | all | add [name] [phone] | "\
                  "change [name] [phone] | contact [name] | delete [name] | "\
                  "add-birthday [name] [date] | show-birthday [name] | birthdays | "\
                  "exit | close")

    # call save before exit
    save_data(book)

if __name__ == "__main__":
    main()
