"""
This is a console helper bot that recognizes commands entered
from the keyboard and responds to this command.
"""


import re


# A decorator block to handle user input errors.
def input_error(func):
    def inner(arguments):
        try:
            result = func(arguments)
            return result
        except KeyError:
            return 'Wrong arguments!'
        except TypeError:
            return 'Wrong command!'
    return inner


# In this block, the bot saves a new contact in memory.
def add_contact(name, phone):
    if name in contacts:    # Checking for an already existing name in memory
        return f'Contact with {name} already created. Try to change it.'
    match = re.match(r'\+\d{12}', phone)    # Pattern for phone number
    if match:    # If number matches the pattern
        contacts[name] = phone    # Add new contact with name and phone number
        return f'New contact {name} with number {phone} has been added'
    else:   # If phone number doesn't match pattern
        return 'Incorrect number! Write in the format: +380123456789'


def advice():
    instruction = "How can I help you?"
    return instruction


# This function changes phone number in a existing contact
def change_number(name, phone):
    if name in contacts:    # Checks that contact with given name is exist
        contacts[name] = phone    # Number changing
        return f'Contact {name} has been changed'
    else:    # If contact with name doesn't exist
        return f'{name} does not exist in contacts. Try to create new contact.'


def close_bot():
    instruction = 'Good bye!'
    return instruction


# Currying
@input_error
def handler(command):
    if command in COMMANDS:
        return COMMANDS[command]
    else:
        return COMMANDS_WITHOUT_ARGS[command]


# Shows all contacts
def get_contacts():
    return contacts


# Shows all phone numbers
def get_phone(name):
    return f"{name}'s phone number is {contacts[name]}"


# Handling user commands
@input_error
def reply(user_command):
    if user_command.lower() not in COMMANDS_WITHOUT_ARGS:    # Checking if given command has arguments
        command, args = user_command.split(' ')[0].lower(), user_command.split(' ')[1:]    # Separate command, arguments
        instruction = handler(command)    # Instruction is a signature of given function by user
        return instruction(*args)    # Execute command with arguments given by user
    else:
        return handler(user_command.lower())()    # Execute command without any arguments


# List of commands that don't take arguments and their command-words
COMMANDS_WITHOUT_ARGS = {
    'close': close_bot,
    'exit': close_bot,
    'good bye': close_bot,
    'hello': advice,
    'show all': get_contacts,
}
# # List of commands that take arguments and their command-words
COMMANDS = {
    'add': add_contact,
    'change': change_number,
    'phone': get_phone,
}
# Book of contacts
contacts = {}


def main():
    bot_loop = True
    while bot_loop:
        user_input = input('>> ')
        if handler(user_input.lower()) == close_bot:    # If the command entered is to exit the program
            bot_loop = False    # Stop loop
        print('<<', reply(user_input))


if __name__ == '__main__':
    main()
