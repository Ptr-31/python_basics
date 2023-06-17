# Check if a password, which is a string input is secure
# at least one capital letter
# at least one small letter
# at least one number
# at least 12 characters
# no repeated letters or numbers (example: 123; ABC)

#implement an algorithm for checking password complexity. Bonus: Try using regex.
#Also make sure that the password has not leaked . You can use the haveibeenpwned API

import hashlib
import requests
def password_characters(password: str):
    lowercase_alphabet = [i for i in range(ord('a'), ord('z')+1)]
    capital_letters = [i for i in range(ord('A'), ord('Z')+1)]
    numbers = [i for i in range(ord('0'), ord('9')+1)]
    pass_characters_dict = dict.fromkeys(['capital_letters', 'lowercase_letters',
                                          'numbers', 'characters'], 0)
    for item in password:
        if ord(item) in lowercase_alphabet:
            pass_characters_dict['lowercase_letters'] += 1
        elif ord(item) in capital_letters:
            pass_characters_dict['capital_letters'] += 1
        elif ord(item) in numbers:
            pass_characters_dict['numbers'] += 1
    pass_characters_dict['characters'] = len(password)
    # print(pass_characters_dict)
    if pass_characters_dict['lowercase_letters'] >= 1 and \
            pass_characters_dict['capital_letters'] >= 1 and \
            pass_characters_dict['numbers'] >= 1 and \
            pass_characters_dict['characters'] >= 11:
        return True, pass_characters_dict
    else:
        return False, pass_characters_dict

def repeated_items(password:str) -> bool:
    temp_bool = False
    for i in range(0, len(password) - 2):
        if(ord(password[i]) == ord(password[i+1]) - 1 == ord(password[i+2]) - 2):
            temp_bool = True
        elif((ord(password[i]) == ord(password[i+1]) == ord(password[i+2]))):
            temp_bool = True
    return temp_bool

def leadked_pass(password: str):
    hasH = hashlib.sha1(password.encode('utf-8')).hexdigest()
    hasH = hasH.upper()
    hasH_prefix = hasH[:5]
    hasH_postfix = hasH[5:]
    status_code = 200
    link = 'https://api.pwnedpasswords.com/range/'
    responce = requests.get(link + hasH_prefix)
    if responce.status_code == status_code:
        responce_text = responce.text.splitlines()
        for item in responce_text:
            if item[:35] == hasH_postfix:
                return False
        return True
    else:
        print('Status call = ', responce.status_code, 'password leak check is not available')

def complex_password_checking(password: str):
    bool_pass_characters, dict_pass_characters = password_characters(password)
    if bool_pass_characters:
        if repeated_items(password):
            print('Password isn\'t good, it\'s repeating!')
        else:
            if leadked_pass(password):
                print('Password is good! Ready to use')
            else:
                print('Password isn\'t good, it\'s leaked')
    else:
        print('Password isn\'t good')
        print('It has only: \n' + str(dict_pass_characters['lowercase_letters']) + ' lowercase letters\n' +
              str(dict_pass_characters['capital_letters']) + ' upper case letter(s)\n' +
              str(dict_pass_characters['numbers']) + ' numbers\n' +
              str(dict_pass_characters['characters']) + ' characters')

def main():
    complex_password_checking('7INmpQywO?v}bz')
if __name__ == "__main__":
    main()