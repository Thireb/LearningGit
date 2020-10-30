# python
'''
Documentation of password manager
Check if there's a master password
if not then create a new user and master password
if exists then show all of the passwords
Ask to save a new password
Ask to generate a random password
'''
import csv
import os
import random
import string
import sys


def startup():
    # call login wizard, for new login
    # print('inside startup')
    directory = os.path.join(os.getcwd(), 'PasswordVault')
    master_pass = ''
    # try:
    # print('inside try')
    #   with open('masterpassword_file.txt') as read_pass:
    #      data = read_pass.readlines()
    # print(master_pass)
    # except Exception as e:
    #   print('No previous data found....')

    # filePath = os.path.join(directory, 'masterpassword_file.txt')
    # print(filePath)
    # print(os.path.exists(filePath))
    # print(os.path.exists(directory))
    # print(os.path.exists('masterpassword_file.txt'))
    if os.path.exists('masterpassword_file.txt') and os.path.exists(directory):
        print('File and directory exists....')
        with open('masterpassword_file.txt') as read_pass:
            data = read_pass.readlines()
            # print(data)
        password = input('Enter the master password: ')
        dir_change(directory)  # Directory change has occured
        file_name = data[1]+'_passwords.csv'
        if os.path.exists(file_name):
            if password == data[0].strip():
                reader(file_name)
                ans = input('Wanna save another password? Y/N')
                if ans in ['Y', 'y', 'yes', 'Yes']:
                    user_data = getting_info()
                    old_file_input(user_data, file_name)
                    reader(file_name)
                    print('Bye.......')
                    sys.exit()
                else:
                    print('Bye-------')
                    sys.exit()
        else:
            print('No password file found. Let\'s create a new one.')
            # master_pass, user_name = new_login()  # get name and pass
            # store_masterpass(master_pass, user_name)
            # folder_creation(directory)  # create folder
        # store master pass in the designated directory
            file_name = data[1]+'_passwords.csv'  # repeating line
            user_data = getting_info()  # Take information
            new_file_input(user_data, file_name)
            # wanna save another file? append to old file then using if
            ans = input('Save password? Y/N')
            if ans in ['Y', 'y', 'yes', 'Yes']:
                user_data = getting_info()  # Take information
                # append to end of data file created above
                old_file_input(user_data, file_name)
                reader(file_name)
                print('Bye.......')
                sys.exit()
            else:
                print('Bye______')
                sys.exit()
    else:

        print('No previous data found.\nYou seem to be a new user. Let\'s get you started then.')
        master_pass, user_name = new_login()  # get name and pass
        store_masterpass(master_pass, user_name)
        folder_creation(directory)  # create folder
        # store master pass in the designated directory

        file_name = user_name+'_passwords.csv'  # repeating line
        user_data = getting_info()  # Take information
        new_file_input(user_data, file_name)
        # wanna save another file? append to old file then using if
        reader(file_name)
        ans = input('Save password? Y/N')
        if ans in ['Y', 'y', 'yes', 'Yes']:
            user_data = getting_info()  # Take information
            # append to end of data file created above
            old_file_input(user_data, file_name)
            reader(file_name)
            print('Bye!')
            sys.exit()
        else:
            print('Bye')
            sys.exit()


'''
    if len(master_pass) == 0 or len(data[0]) == 0:
        master_pass, user_name = new_login()  # get name and pass
        store_masterpass(master_pass, user_name)
        folder_creation(directory)  # create folder
        # store master pass in the designated directory

        file_name = user_name+'_passwords.csv'  # repeating line
        user_data = getting_info()  # Take information
        new_file_input(user_data, file_name)
        # wanna save another file? append to old file then using if
        ans = input('Wanna save another password? Y/N')
        if ans in ['Y', 'y', 'yes', 'Yes']:
            user_data = getting_info()  # Take information
            # append to end of data file created above
            old_file_input(user_data, file_name)
            reader(file_name)
            print('Bye.......')
            sys.exit()
        else:
            sys.exit()
    else:
            # for old login
        # change directory first and check if it exists
        password = input('Enter the master password: ')
        dir_change(directory)
        file_name = data[1]+'_passwords.csv'
        if password == data[0].strip():
            reader(file_name)
            ans = input('Wanna save another password? Y/N')
            if ans in ['Y', 'y', 'yes', 'Yes']:
                user_data = getting_info()
                old_file_input(user_data, file_name)
                reader(file_name)
                print('Bye.......')
                sys.exit()
            else:
                sys.exit()
'''


def dir_change(directory):
    if os.path.exists(directory):
        os.chdir(directory)
        print('Directory change successful...')


def new_login():
    # Create a new Master
    # print("You seem to be a new user...Let's get you started then.")
    user_name = input('Enter your Name, it is case sensitive: ')
    master_pass = input('Enter master password: ')

    print("If you forget the master password, it'll break your heart..\n")
    print("Welcome.....")

    return master_pass, user_name


def getting_info():
    # Storing the information of the user
    web_site = input('Website name?..: ')
    user_name = input('Username or Login ID: ')
    pass_word = input('Enter password or type Gen to generate a password..: ')
    if pass_word in ['Gen', 'gen']:
        pass_word = passwordGen(11)
    print('Password is: '+pass_word)
    e_mail = input('Enter the Email for the Site.: ')
    # user_info_dictVer = {'Website': web_site,
    #                    'Username': user_name, 'Password': pass_word, 'Email': e_mail}
    data_list = [web_site, user_name, pass_word, e_mail]
    return data_list
    #
    # new_file_input(user_info_dictVer, file_name, file_Header)
    # user_info = []
    # user_info.append(web_site)
    # user_info.append(user_name)
    # user_info.append(pass_word)
    # user_info.append(e_mail)
    # print(user_info)


def folder_creation(directory):
    # create a new folder to save the csv file to
    # folder = 'PasswordMangerVault_'+user_name
    os.makedirs(directory, exist_ok=True)
    os.chdir(directory)
    print('Folder created and directory changed...')
    # directory = os.path.join(os.getcwd(), folder)
    # return directory


def store_masterpass(master_pass, user_name):
    with open('masterpassword_file.txt', 'w') as passfile:
        passfile.write(master_pass+'\n')  # first store the master password
        passfile.write(user_name)  # then store the user name
    print('Master password and username saved.')


def new_file_input(user_dict, file_name):
    # Create a csv file and add data to it

    with open(file_name, 'w', newline='') as simple_file:
        # simple_file = open('ahmad_passwords.csv', 'w')
        headers = ['Website', 'LoginID/Username', 'Password', 'Email']
        writer_Object = csv.writer(simple_file)
        writer_Object.writerow(headers)
        writer_Object.writerow(user_dict)
        # write_able = csv.DictWriter(simple_file, fieldnames=fieldnames)
        # write_able.writeheader()
        # write_able.writerow(user_dict)


def old_file_input(user_dict, file_name):
    # open the file again to append data in it
    # fieldnames = ['Website ', 'Username ', 'Password ', 'Email ']
    with open(file_name, 'a', newline='') as append_file:
        # append_Dict = csv.DictWriter(append_file, fieldnames=fieldnames)
        # append_Dict.writerow(user_dict)
        append_object = csv.writer(append_file)
        append_object.writerow(user_dict)


def reader(file_name):
    # Search in the csv file to retrive data
    with open(file_name) as read_file:
        # print('inside reader')
        reader_object = csv.reader(read_file)
        reading = list(reader_object)

       # for line in reading:
        # print(line)
        if len(reading) == 0:
            print('File is empty...')
        else:
            for line in reading:
                print(line)
    print('Data Reading Finished. Showing all saved data.')


def passwordGen(num):
    password = ''
    while True:
        for n in range(num):
            x = random.randint(0, 94)
            password += string.printable[x]
        ans = input('Is it okay?\n' + password + '\n(Y/N): ')
        if ans in ['y', 'Y', 'Yes', 'yes']:
            break
        else:
            continue
    return password


# Create login for the whole programme.
# put checks in places for errors
startup()
# passwordGen(16)
