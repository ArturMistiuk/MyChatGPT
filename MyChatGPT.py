import re


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


def add_contact(name, phone):
    if name in contacts:
        return f'Contact with {name} already created. Try to change it.'
    match = re.match(r'\+\d{12}', phone)
    if match:
        contacts[name] = phone
        return f'New contact {name} with number {phone} has been added'
    else:
        return 'Incorrect number! Write in the format: +380123456789'


def advice():
    instruction = "How can I help you?"
    return instruction


def change_number(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f'Contact {name} has been changed'
    else:
        return f'{name} does not exist in contacts. Try to create new contact.'


def close_bot():
    instruction = 'Good bye!'
    return instruction


@input_error
def handler(command):
    if command in COMMANDS:
        return COMMANDS[command]
    else:
        return COMMANDS_WITHOUT_ARGS[command]


def get_contacts():
    return contacts


def get_phone(name):
    return f"{name}'s phone number is {contacts[name]}"


@input_error
def reply(user_command):
    if user_command.lower() not in COMMANDS_WITHOUT_ARGS:
        command, args = user_command.split(' ')[0].lower(), user_command.split(' ')[1:]
        instruction = handler(command)
        return instruction(*args)
    else:
        return handler(user_command.lower())()


COMMANDS_WITHOUT_ARGS = {
    'close': close_bot,
    'exit': close_bot,
    'good bye': close_bot,
    'hello': advice,
    'show all': get_contacts,
}
COMMANDS = {
    'add': add_contact,
    'change': change_number,
    'phone': get_phone,
}
contacts = {}


def main():
    bot_loop = True
    while bot_loop:
        user_input = input('>> ')
        if handler(user_input.lower()) == close_bot:
            bot_loop = False
        print('<<', reply(user_input))


if __name__ == '__main__':
    main()
