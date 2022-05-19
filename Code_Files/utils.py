import requests
import pandas as pd
import numpy as np
from tabulate import tabulate
import connect_db


class api:

    def __init__(self):
        self.api_key_tomtom = 'IRw2IHAJbL34s8WgUK0LJXmAGwtHjGwF'
        self.api_key_geocoding = 'MThkNjNjYWMxMWRmNDQxMWFhMzdhYzA0YzI3NzMwZDQ6MDg0OGRkZGQtN2FiZi00OTE2LTg4M2ItMTM2MzJkNDRhZWEw'
        self.api_key_yelp = '1dU6Q3s0JGTMQHbcGM1AhMD2U083gufXqvIEBADCdjyEgD5Yx-oSV-ro0TIv1JzKORsBHYy50iNTi13G8wgYUCzzIn_-ZKWi_2lndstW37vvSC8LYS686MtqZyRoYnYx'
        self.endpoint_geocoding = 'https://api.myptv.com/geocoding/v1/locations/by-text'
        self.endpoint_tomtom = 'https://api.tomtom.com/search/2/categorySearch/'
        self.endpoint_yelp = 'https://api.yelp.com/v3/businesses/search'

    def get_api_response(self, endpoint, headers, params):
        try:
            response = requests.get(url=endpoint, headers=headers, params=params)
            response_data = response.json()
            return response_data
        except Exception as e:
            print('API error.', e)


class utilities:
    def user_input(self, query):
        q = input(query)
        return q

    def view_menu(self):
        try:
            print('\n_____________________YOUR ESCAPADE SEARCH MENU_____________________________\n\n')
            menu = {1: 'Attractions', 2: 'Restaurants',
                    3: 'Experience Nature', 4: 'Shopping', 5: 'Hotels', 0: 'Return to Main Menu'}
            return menu
        except Exception as e:
            print(e)

    def view_main_menu(self):
        try:
            print('\n_____________________YOUR ESCAPADE MAIN MENU_____________________________\n')
            main_menu = {1: 'Search', 2: 'Help', 0: 'Exit Application'}
            return main_menu

        except Exception as e:
            print(e)

    def login_or_register(self):
        try:
            print('_____________________LOGIN OR REGISTER_____________________________\n\n')
            login_menu = {'Option': [1,2], 'Name': ['Register','Login']}
            print(tabulate(login_menu, headers = "keys"),'\n')
            return login_menu
        except Exception as e:
            print(e)

    def create_table(self, search_result):
        try:
            df = pd.DataFrame(search_result)
            df.index = np.arange(1, len(df) + 1)
            return df
        except Exception as e:
            print(e)


## Please start code here
def homepage():                                                      # need a register and log in option when users enter program
    try:
        log=utilities()
        log.login_or_register()
        hello = input("What would you like to do: ")
        if hello == "1":
            usr=register()
            return usr
        elif hello == "2":
            usr=login()
            return usr
        else:
            print("Please choose a valid option")
            homepage()
    except Exception as e:
        print(e)

def register():
    try:
        user_exists=True
        email_exists=True
        password_validity=False
        name=''
        email_address=''
        while user_exists:
            name = input("User Name: ")
            user_exists=connect_db.check_user_exists(name,'USER_NAME')
            if user_exists:
                print('User Name already exists')

        while email_exists:
            email_address = input("Email address: ")
            email_exists=connect_db.check_user_exists(email_address,'EMAIL_ADDRESS')
            if email_exists:
                print('Email already exists')

        while password_validity == False:
            password = input("Password: ")
            password_validity = password_checker(password)
            if password_validity:
                connect_db.insert_new_users(name, email_address, password)
                record=connect_db.get_all_records(email_address)
            else:
                print("Password entered does not meet requirements. \n The requirements: a special character,a number, a capital and must be greater than 5 characters")

        new_user = user(record[0][0], name, email_address, password)
        print("Welcome, " + new_user.name)
        return new_user
    except Exception as e:
        print(e)

def login():
    try:
        login_result=0
        while login_result==0:
            login_email = input("Email address: ")
            login_password = input("Password: ")
            login_result=connect_db.password_from_inputted_username(login_email,login_password)
            if login_result == 0:
                print("Incorrect email or password. Please enter your details again.")

        print("Welcome, " + login_result.name)
        usr=user(login_result.user_id,login_result.name,login_result.email_address,login_result.password)
        return usr

    except Exception as e:
        print(e)


def password_checker(registeredpassword):
    try:
        numerics = '0123456789'
        capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_characters = "!$£&%*:;@#~+=-_^"
        sum = 0
        w = 0
        x = 0
        y = 0
        z = 0
        while sum != 4:
            # while len(password) != 5:
            #     password = input("Please enter a correct password")

            for i in range(len(registeredpassword)):
                if len(registeredpassword) > 5:
                    w = 1
                if registeredpassword[i] in numerics:
                    x = 1
                if registeredpassword[i] in capitals:
                    y = 1
                if registeredpassword[i] in special_characters:
                    z = 1
            sum = w + x + y + z
            if sum == 4:
                print("\nPassword is accepted")
                return True

            else:
                return False

    except Exception as e:
        print(e)


class user:
        def __init__(self,user_id,name,email_address,password):
                self.user_id=user_id
                self.name=name
                self.email_address=email_address
                self.password=password

       
      









