import random
import string
def details():
    first_name = input("Input your First Name: ")
    last_name = input("Input your Last Name: ")
    email = input("input your email: ")
    user_details = [first_name, last_name, email]
    return user_details
def password(user_details):
    letters = string.ascii_letters
    length = 5
    auto_pasword = ''.join(random.choice(letters) for i in range(length))
    gen_password = str(user_details[0][0:2] + user_details[1][-2:] + auto_pasword)
    return gen_password
data = True
storage = []
while data:
    user_details = details()
    gen_password = password(user_details)
    print("Your random password is " + str(gen_password))
    change_password = input( "Are you satisfied with this password or would you like to change it.\n"
                             "If No, please do put in your new password: ")
    while change_password.upper() == 'YES':
        user_details.append(gen_password)
        storage.append(user_details)
        break
    else:
        new_password = input("Enter Password Longer than or equal to 7")
        password_length = True
        while password_length:
            if len(new_password) >= 7:
                user_details.append(new_password)
                storage.append(user_details)
                password_length = False
            else:
                print("Your password is less than 7")
                new_password = input(str("Password should be more than 7 characters"))
    new_details = input("Do you want to a New Detail? Yes or No: ")
    if new_details.upper() == "YES":
        status = True
    else:
        stat = False
        for items in storage:
            print(items)