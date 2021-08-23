import os
import json
import getpass
PWDB_FILENAME = 'pwdb.json'

def get_credentials():
    username = input('Type the username: ')
    password = getpass.getpass(prompt = 'Type the password: ')
    hashed_password = pwhash(password)
    return username, hashed_password

def add_user(user, password, pwdb):
    pwdb[user] = password
    write_pwdb(pwdb)
    return


def authenticate(user, password, pwdb):
    if user in pwdb:
        if password == pwdb[user]:
            print('Successfully authenticated!')
        else:
            print('Wrong password!!')
    else:
        answer = input('Add user to the db? ')
        if answer == 'y':
            add_user(user, password, pwdb)

    return


def pwhash(password):
    hash_ = 0
    for idx, char in enumerate(password):
        hash_ += (idx+1)*ord(char)
    return hash_


def write_pwdb(pwdb):
     with open(PWDB_FILENAME, 'w') as fh:
        json.dump(pwdb, fh)

def read_pwdb():
    if os.path.exists(PWDB_FILENAME):
        with open(PWDB_FILENAME, 'r') as fh:
            pwdb = json.load(fh)
    else:
        pwdb = {}
        write_pwdb(pwdb)
    return pwdb


if __name__ == "__main__":
    pwdb = read_pwdb()
    user, password = get_credentials()
    authenticate(user, password, pwdb)
    write_pwdb(pwdb)
    print(pwdb)

