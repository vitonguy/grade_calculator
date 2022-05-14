import email_storage as es

# creates domain file
f = open('domain_storage.txt', 'a+')
f.write('Domains:\n')
f.close()

# creates username file
f = open('username_storage.txt', 'a+')
f.write('Usernames:\n')
f.close()

while True:
    '''asks for email until user indicates stop'''
    # ask for email and gives option to quit the program
    email = input('Please enter your email or type n to quit: ')
    if email == 'n':
        break

    # target values in email
    commercial_at = email.index('@')
    period = email.index('.')

    # removes the period and following in email
    email = email.strip(email[period:])

    # finds domain from email and stores it
    domain = email[commercial_at+1:]
    es.store(domain, 'domain')

    # finds username in email and stores it
    username = email[:commercial_at]
    es.store(username, 'username')
