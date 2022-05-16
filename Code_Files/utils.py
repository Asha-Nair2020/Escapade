import requests
import pandas as pd
import numpy as np
from connect_db import password_from_inputted_username, insert_new_users


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
            menu = {1: 'Attractions', 2: 'Restaurants',
                    3: 'Experience Nature', 4: 'Shopping', 5: 'Hotels', 0: 'Return to Main Menu'}
            return menu
        except Exception as e:
            print(e)

    def view_main_menu(self):
        try:
            main_menu = {1: 'Search', 2: 'Help', 0: 'Exit Application'}
            return main_menu

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



class user:
        def __init__(self,name,email_address,password,phone_number,recovery_email):
                self.name=name
                self.email_address=email_address
                self.password=password
                self.phone_number=phone_number
                self.recovery_email=recovery_email
       
      


        # need a register and log in option when users enter program


        def homepage(user):
            print("Login OR Register")
            hello = input("What would you like to do: ")
            if hello == "Register":
                register()
            elif hello == "Login":
                login(user)
            else:
                print("Please choose a valid option")
                homepage(user)


        def register():
            name = input("Name: ")
            email_address = input("Email address: ")
            password = input("Password: ")
            # phone = int(input("Phone number: "))
            # recovery_email = input("Alternative recovery email address: ")
            new_user = User(name, email_address, password)
            print("Welcome, " + new_user.name)
            homepage(new_user)


        def login(user):
            login_email = input("Email address: ")
            login_password = input("Password: ")

            if login_password == user.password:
                print("Welcome, " + user.name)
            else:
                print("Incorrect username or password")
                login(user)
            homepage('')
        

        def password_checker(registeredpassword):
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
                                print("Password is accepted")
                                ##use serial for user id = wont have to  add this in
                                record = {
                                        "USER_NAME": registeredname,
                                        "USER_PASSWORD": registeredpassword
                                }
                                insert_record(record, registeredname)

                        else:
                                print(
                                        "Password entered does not meet requirements. \n The requirements: a special character, a capital and must be greater than 5 characters")
                                registeredpassword = input("Please enter a correct password: ")


class escapade_db(user):



homepage('')


class escapade_db(User):
    pass
