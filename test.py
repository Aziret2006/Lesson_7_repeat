# test 1
intgear = 12
float_ = 122.2
string = "abcdefg"
bool_ = True, False, None
lists = [1, 2.3, "sally", True]
tuple_ = ('Tuple', 1, 2)

# task 2
from random import randint
while True:
    num = randint(0, 1)  # randoom.random()
    if num == 0:
        print("Да")
    else:
        print("Нет")
        break
# task 3
ls = list(range(10, 200, 10))
# for i in range(0, 200, 10):
#     ls.append(i)
print(ls)

# Main task

# database_login = []
# database_password = []
# basename = []
all_users = [
    ('Admin', 'Adminov', '21', '0 (312) 705-070', 'admin', 'admin')

]
while True:
    action = input(""" 
1. Регистрация введите 1 
2. Авторизация введите 2 
3. Выйти введите 3 
""")


    if action == '1':
        username = input("Enter your username")
        password = input("Enter your password")

        client_is_exist = [user[-2] == username for user in all_users]

        error_message = 'Incorrect username or password'
        if any(client_is_exist):
            client_id = client_is_exist.index(True)
            my_client = all_users[client_id]
            if my_client[-1] == password:
                print('Authorization was succesfuly!')
            else:
                print(error_message)
        else:
            print(error_message)
    elif action == '2':
        name = input('Enter name:').strip()
        surname = input("Enter surname: ").strip()
        age = input("Enter age: ").strip()
        phone_number = input("Enter phone number, Example (0558705070):  ").strip()

        is_valid = []

        if name.isalpha() and 15 > len(name) >= 2:
            name = name.capitalize()
            is_valid.append(True)
        else:
            is_valid.append(False)
            print('First name was entered incorrect!')

        if surname.isalpha() and 15 > len(surname) >= 2:
            surname = surname.capitalize()
            is_valid.append(True)
        else:
            is_valid.append(False)
            print('Last name was entered incorrect!')

        if age.isdigit() and 150 > int(age) > 0:
            age = int(age)
            is_valid.append(True)
        else:
            is_valid.append(False)
            print('Age was entered incorrect!')

        if phone_number.isdigit() and 10 == len(phone_number):
            phone_number = phone_number[0] + '(' + phone_number[1:4] + ')' + phone_number[4:8] + '-' + phone_number[8:]
            is_valid.append(True)
        else:
            is_valid.append(False)
            print('Phone number was entered incorrect (Example:0558705070) ')

        if all(is_valid):

            is_registred = False
            for chance_count in range(5, 0, -1):
                username = input('Enter username: ')

                is_unique = all([user[-2] != username for user in all_users])

                if is_unique:
                    for password_chance_count in range(5, 0, -1):
                        password = input('Please enter your password(there should be more 8): ')
                        conf_password = input('Please enter your password: ')
                        if len(password) >= 8:
                            if password == conf_password:
                                all_users.append(
                                    (name, surname, age, username, conf_password)
                                )
                                print(f"Registration was success! See you {name}")
                                break
                            else:
                                print("Password missmatch You have {password_chance_count} chance!\n\n")
                        else:
                            print(
                                f"Password has {len(password)} symbols! Min symbols password is 8! You have {password_chance_count} chance!\n\n")
                else:
                    print(f"Username {username} is exist! Try another username! You have {chance_count} chance!\n\n")
                if is_registred:
                    break
        else:
            print('Please try registration again with edit wrong')

    elif action == '3':
        print('Goodbye! See you')
        break
    else:
        print('Please enter correct '
            '1. Регистрация введите 1 '
            '2. Авторизация введите 2 '
            '3. Выйти введите 3 ')

# choice = input("Введите что выбрали: ")
    # if choice == '1':
    #     name = str(input("Enter name: ").strip())  # Запрашиваем имя
    #     surname = str(input("Enter surname: ").strip())  # Запрашиваем фамилию
    #     check_names = name.isalpha() and surname.isalpha()
    #     if not check_names:
    #         print("The name or surname must contain only letters")
    #         continue
    #     basename.append(name)
    #     age = input("Enter age: ").strip()  # Запрашиваем BозрасT
    #     if not age.isdigit():
    #         print("Enter only numbers")
    #         continue
    #
    #     number = input("Enter phone number: + ").strip()  # Запрашиваем номер
    #     num = number.replace(" ", "")
    #     check_number = len(num) == 12 or len(num) == 13 and (num.startswith('996'))
    #     if not check_number:
    #         print("Invalid number")
    #         continue
    #
    #     login = input("Enter login(должно быть больше 6):").strip().lower()  # Запрашиваем логин
    #     password = input("Enter password(должно быть больше 8): ").strip()  # Запрашиваем пароль
    #     check_password_login = len(login) >= 6 and len(password) >= 8
    #     if not check_password_login:
    #         print("Invalid login or password")
    #         continue
    #     database_login.append(login)
    #     database_password.append(password)
    #
    #     for j in range(3):
    #         password_confirmation = input("Enter confirm password: ").strip()  # Запрашиваем подверждение пароля
    #
    #         if password_confirmation == password:
    #             print("Welcome")
    #             break
    #         else:
    #             print("Your password does not match")
    #             continue
    #     else:
    #         print("You don't have attemts!")
    #
    # elif choice == '2':
    #     confrim_log = input('Enter your login: ')
    #     confrim_pas = input('Enter your password: ')
    #     if confrim_pas == database_password and database_login == confrim_log:
    #        print("Hello", basename)
    #     else:
    #         print("Your login or password does not match")
    #         continue
    # elif choice == '3':
    #     print("Goodbye")
    #     break
    # else:
    #     print("Choose 1, 2, 3 !")
    #     continue
    #
