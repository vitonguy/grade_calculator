# stores text based on indicated part of an email

def store(email_part, domain_or_username):
    '''stores the domain or username of the email'''
    print(f'The {domain_or_username} is {email_part}')

    # prep to later check if the domain/username is in storage
    with open(f'{domain_or_username}_storage.txt') as file_object:
        lines = file_object.readlines()

    string = ''
    for line in lines:
        string += line.strip()

    # prompt to ask to add domain/username
    if email_part in string:
        print(f'There is already a {domain_or_username} like this!')
    else:
        print(f'The {domain_or_username} does not appear to be in the storage, would you like to add it?')
        answer = input('Please reply with y or n: ')
        if answer == 'y':
            with open(f'{domain_or_username}_storage.txt', 'a') as file_object:
                file_object.write(f'{email_part}\n')
            print('Stored!')
        else:
            print(f'The {domain_or_username} has not been added.')