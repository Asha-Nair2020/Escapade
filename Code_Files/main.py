import pandas as pd
from art import logo
import utils
from connect_db import _connect_to_db

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 7000)

print(logo, '\n Welcome to the joys of London!\n', )


def main():
    try:
        while 1 == 1:
            # # 1. Create objects
            utl_obj = utils.utilities()
            api_obj = utils.api()
            # Show Menu
            main_menu = utl_obj.view_main_menu()
            main_menu_df = pd.DataFrame(main_menu.items())
            main_menu_df.columns = ['Option', 'Name']
            main_menu_df = main_menu_df.set_index(['Option'])
            print(main_menu_df)
            main_menu_option = utl_obj.user_input('Choose an option:')
            if main_menu_option == '1':
                sub_menu = utl_obj.view_menu()
                sub_menu_df = pd.DataFrame(sub_menu.items())
                sub_menu_df.columns = ['Option', 'Activity']
                sub_menu_df = sub_menu_df.set_index(['Option'])
                print(sub_menu_df)

                # 3. Users selects option
                option = utl_obj.user_input('What are you looking for today? ')

                if option == '1' or option == '3' or option == '5':
                    user_location = utl_obj.user_input('Please enter your location and city or post_code: ')

                    parameters = {'searchText': user_location,
                                  'apiKey': api_obj.api_key_geocoding
                                  }
                    data = api_obj.get_api_response(api_obj.endpoint_geocoding, None, parameters)

                    coordinates_lat = data['locations'][0]['referencePosition'][
                        'latitude']  # Fetches the latitude of the lccation entered
                    coordinates_longitude = data['locations'][0]['referencePosition'][
                        'longitude']  # Fetches the longitude of the lccation entered

                    # 5. call tomtom api wit hte lat, lon and the option selected
                    params = {
                        'limit': 25,
                        'radius': 5000,
                        'countrySet': 'GBR',
                        'lat': str(coordinates_lat),
                        'lon': str(coordinates_longitude),
                        'key': api_obj.api_key_tomtom,
                        'view': 'Unified',
                        'relatedPois': 'off'
                    }

                    results_json = api_obj.get_api_response(api_obj.endpoint_tomtom + sub_menu[int(option)] + '.json',
                                                            None, params)

                    category_results = []
                    for i in range(len(results_json['results'])):
                        category_dict = {}
                        category_dict['NAME'] = results_json['results'][i]['poi']['name']
                        category_dict['ADDRESS'] = results_json['results'][i]['address']['freeformAddress']
                        category_dict['CATEGORY'] = results_json['results'][i]['poi']['categories'][0].title()
                        if 'phone' in results_json['results'][i]['poi']:
                            category_dict['PHONE'] = results_json['results'][i]['poi']['phone']
                        else:
                            category_dict['PHONE'] = ''
                        category_results.append(category_dict)
                    print(utl_obj.create_table(category_results))
                    activity_choice = utl_obj.user_input('Where would you like to go? '
                                                         'Kindly enter the index of the place. Thank you.')
                    recommendation = input("Are you happy with recommendation please only select one: Yes/No")
                    if activity_choice:
                        if recommendation == "No" or "no":
                            activity_choice = utl_obj.user_input('Where would you like to go? '
                                                                 'Kindly enter the index of the place again. Thank you.')
                            recommendation = input("Are you happy with recommendation please ony select one: Yes/No")
                        if recommendation == "Yes" or "yes":
                            print("This recommendation will save to your favourites now!")
                        else:
                            print("Please try again")


                    # Please call the function to insert activity choice to the database.>

                elif option == '2' or option == '4':
                    user_location = utl_obj.user_input('Please enter your location and city: ')
                    headers = {
                        'Authorization': 'Bearer %s' % api_obj.api_key_yelp
                    }

                    parameters = {'location': user_location,
                                  'term': sub_menu[int(option)],
                                  'radius': 2000,
                                  'limit': None}

                    data1 = api_obj.get_api_response(api_obj.endpoint_yelp, headers, parameters)

                    results = []
                    for i in range(len(data1['businesses'])):
                        features = {}
                        features['NAME'] = data1['businesses'][i]['name']
                        features['TYPE'] = data1['businesses'][i]['categories'][0]['title']
                        features['PRICE'] = '' if 'price' not in data1['businesses'][i] else data1['businesses'][i][
                            'price']
                        features['RATING'] = data1['businesses'][i]['rating']
                        features['REVIEW_COUNT'] = data1['businesses'][i]['review_count']
                        features['IS_OPEN'] = 'Yes' if data1['businesses'][i]['is_closed'] == False else 'No'
                        features['ADDRESS'] = ','.join(data1['businesses'][i]['location']['display_address'])
                        features['PHONE'] = data1['businesses'][i]['display_phone']
                        results.append(features)
                    print(utl_obj.create_table(results))

                    activity_choice1 = utl_obj.user_input('Where would you like to go? '
                                                          'Kindly enter the index of the place. Thank you.')
                    recommendation1 = input("Are you happy with recommendation please only select one: Yes/No")
                    if activity_choice1:
                        if recommendation1 == "No" or "no":
                            activity_choice1 = utl_obj.user_input('Where would you like to go? '
                                                                 'Kindly enter the index of the place again. Thank you.')
                            recommendation1 = input("Are you happy with recommendation please ony select one: Yes/No")
                        if recommendation1 == "Yes" or "yes":
                            print("This recommendation will save to your favourites now!")
                        else:
                            print("Please try again")

                    ## Please call the function to insert activity choice to the database.

                elif option == '0':
                    main()
                else:
                    print('Sorry, this is not a valid choice.')

            elif main_menu_option == '2':
                print('Customer Support: 02036874453\n Email Address:escapade@gmail.com')

            else:
                print('Thank you for using Escapade.\n')
                rating_option = utl_obj.user_input('Would you like to leave us a rating?Y/N: ')
                if rating_option == 'Y':
                    app_rating = utl_obj.user_input('From 1-5,How would you rate us?')

                    ## <Call the class method to insert application rating to DB.>

                    print('Thank you for rating us. It was a pleasure to serve you.')
                    exit()
                else:
                    exit()
    except Exception as e:
        print(e)
        print('Application Error. Please login again.')
        exit()


if __name__ == '__main__':
    main()
