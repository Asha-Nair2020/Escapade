import requests
import pandas as pd
import numpy as np
class api:

        def __init__(self):
                self.api_key_tomtom='IRw2IHAJbL34s8WgUK0LJXmAGwtHjGwF'
                self.api_key_geocoding='MThkNjNjYWMxMWRmNDQxMWFhMzdhYzA0YzI3NzMwZDQ6MDg0OGRkZGQtN2FiZi00OTE2LTg4M2ItMTM2MzJkNDRhZWEw'
                self.api_key_yelp='1dU6Q3s0JGTMQHbcGM1AhMD2U083gufXqvIEBADCdjyEgD5Yx-oSV-ro0TIv1JzKORsBHYy50iNTi13G8wgYUCzzIn_-ZKWi_2lndstW37vvSC8LYS686MtqZyRoYnYx'
                self.endpoint_geocoding='https://api.myptv.com/geocoding/v1/locations/by-text'
                self.endpoint_tomtom='https://api.tomtom.com/search/2/categorySearch/'
                self.endpoint_yelp='https://api.yelp.com/v3/businesses/search'

        def get_api_response(self,endpoint,headers,params):

                response = requests.get(url=endpoint, headers=headers, params=params)
                response_data = response.json()
                return response_data

class utilities:

        def user_input(self,query):
                q=input(query)
                return q

        def view_menu(self):
                menu ={1: 'Attractions', 2: 'Restaurants',
                             3: 'Nature', 4: 'Shopping', 5: 'Hotels'}
                return menu

        def create_table(self,search_result):
                df = pd.DataFrame(search_result)
                df.index = np.arange(1, len(df) + 1)
                return df

## Please start code here

class user:
        def __init__(self,name,email_address,password,phone_number):
                self.name=name
                self.email_address=email_address
                self.password=password
                self.phone_number=phone_number
        """
        
        
        """
class escapade_db(user):
        """



        """
