import requests
import pandas as pd
import numpy as np
class api:

        def __init__(self):
                #self.api_key_tomtom='IRw2IHAJbL34s8WgUK0LJXmAGwtHjGwF'
                self.api_key_tomtom = 'IRw2IHAJbL34s8WgUK0LJXmAGwtHjGw'
                self.api_key_geocoding='MThkNjNjYWMxMWRmNDQxMWFhMzdhYzA0YzI3NzMwZDQ6MDg0OGRkZGQtN2FiZi00OTE2LTg4M2ItMTM2MzJkNDRhZWEw'
                self.api_key_yelp='1dU6Q3s0JGTMQHbcGM1AhMD2U083gufXqvIEBADCdjyEgD5Yx-oSV-ro0TIv1JzKORsBHYy50iNTi13G8wgYUCzzIn_-ZKWi_2lndstW37vvSC8LYS686MtqZyRoYnYx'
                self.endpoint_geocoding='https://api.myptv.com/geocoding/v1/locations/by-text'
                self.endpoint_tomtom='https://api.tomtom.com/search/2/categorySearch/'
                self.endpoint_yelp='https://api.yelp.com/v3/businesses/search'

        def get_api_response(self,endpoint,headers,params):
                try:
                        response = requests.get(url=endpoint, headers=headers, params=params)
                        response_data = response.json()
                        return response_data
                except Exception as e:
                        print('API error.',e)

class utilities:

        def user_input(self,query):
                q=input(query)
                return q

        def view_menu(self):
                try:
                        menu ={1: 'Attractions', 2: 'Restaurants',
                                     3: 'Experience Nature', 4: 'Shopping', 5: 'Hotels',0:'Return to Main Menu'}
                        return menu
                except Exception as e:
                        print(e)

        def view_main_menu(self):
                try:
                        main_menu ={1: 'Search', 2: 'Help',0:'Exit Application'}
                        return main_menu

                except Exception as e:
                        print(e)

        def create_table(self,search_result):
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
        """
        
        
        """
class escapade_db(user):

        pass



