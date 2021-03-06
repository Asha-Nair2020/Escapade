import pandas as pd
from art import logo
from threading import Event
from sys import exit
import utils
import connect_db

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 7000)

print(logo, '\n Welcome to the joys of London!\n', )

usr=None
def main():
    global usr
    if usr is None:                         #Check if user is logged in already. If so, usr, the user object will not be none.
        usr=utils.homepage()                # Login or register
    last_recommendation=connect_db.get_recent_recommendations(usr.user_id)      # Get last recommendation for logged in user
    if len(last_recommendation) != 0:
        review_option=input('Would you like to review '+last_recommendation[0][2]+' you visted last? Y/N:  ')
        if review_option.upper()=='Y':
            get_review=input('Please write your review here: \n')
            connect_db.insert_review(usr.user_id,last_recommendation[0][0],last_recommendation[0][2],get_review)
            print('Thank you for your review!\n ')

    try:
        while 1 == 1:
            # # 1. Create objects
            utl_obj = utils.utilities()
            api_obj = utils.api()
            # Show Menu
            main_menu = utl_obj.view_main_menu()                # Get main menu
            main_menu_df = pd.DataFrame(main_menu.items())      # COnvert to data frame for better format
            main_menu_df.columns = ['Option', 'Name']
            main_menu_df = main_menu_df.set_index(['Option'])
            print(main_menu_df)                                 # DIsplay main menu
            main_menu_option = utl_obj.user_input('Choose an option:')
            if main_menu_option == '1':                         # Search option selected from main menu
                sub_menu = utl_obj.view_menu()                  # Get search menu
                sub_menu_df = pd.DataFrame(sub_menu.items())
                sub_menu_df.columns = ['Option', 'Activity']
                sub_menu_df = sub_menu_df.set_index(['Option'])
                print(sub_menu_df)                              # Display search menu

                # 3. Users selects option
                option = utl_obj.user_input('What are you looking for today? ')

                if option == '1' or option == '3' or option == '5':         # Attractions , Nature , Hotels - Use Tomtom API
                    user_location = utl_obj.user_input('Please enter your post_code: ')

                    parameters = {'searchText': user_location,
                                  'apiKey': api_obj.api_key_geocoding
                                  }
                    data = api_obj.get_api_response(api_obj.endpoint_geocoding, None, parameters)       # Call Tomtom api to fetch results based on entered post code

                    coordinates_lat = data['locations'][0]['referencePosition'][
                        'latitude']                                                                     # Fetches the latitude of the lccation entered from geocoding api
                    coordinates_longitude = data['locations'][0]['referencePosition'][
                        'longitude']                                                                    # Fetches the longitude of the lccation entered from geocoding api

                    # 5. call tomtom api wit the lat, lon and the option selected
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

                    search_results = []
                    for i in range(len(results_json['results'])):
                        category_dict = {}
                        category_dict['NAME'] = results_json['results'][i]['poi']['name']
                        category_dict['ADDRESS'] = results_json['results'][i]['address']['freeformAddress']
                        category_dict['CATEGORY'] = results_json['results'][i]['poi']['categories'][0].title()
                        if 'phone' in results_json['results'][i]['poi']:
                            category_dict['PHONE'] = results_json['results'][i]['poi']['phone']
                        else:
                            category_dict['PHONE'] = ''
                        search_results.append(category_dict)
                    df = utl_obj.create_table(search_results)

                    if len(df) != 0:
                        print(df)
                        activity_choice = int(utl_obj.user_input('\nKindly enter the index of the place you would like to go: '))
                        selected_spot = df.iloc[activity_choice - 1]
                        recommendation = input("\nAre you happy with recommendation: Yes/No: ")
                        if activity_choice:
                            if recommendation.upper() == "NO":
                                main()
                            if recommendation.upper() == "YES":
                                connect_db.insert_new_recommendation(int(usr.user_id),selected_spot)        # Insert select reccomentation to database
                                print("This recommendation will save to your favourites now!")
                            else:
                                print("Invalid selection")
                    else:
                        print('\nNo results found. Please modify your search')


                   #Call the yelp API for searching restaurants and shopping centres.

                elif option == '2' or option == '4':                      # Restuarants and Shooping - Yelp API
                    user_location = utl_obj.user_input('Please enter your location and city: ')
                    headers = {
                        'Authorization': 'Bearer %s' % api_obj.api_key_yelp
                    }

                    parameters = {'location': user_location,
                                  'term': sub_menu[int(option)],
                                  'radius': 2000,
                                  'limit': None}

                    data = api_obj.get_api_response(api_obj.endpoint_yelp, headers, parameters)        # Call Yelp api based on entered location

                    search_results = []
                    for i in range(len(data['businesses'])):
                        features = {}
                        features['NAME'] = data['businesses'][i]['name']
                        features['TYPE'] = data['businesses'][i]['categories'][0]['title']
                        features['PRICE'] = '' if 'price' not in data['businesses'][i] else data['businesses'][i][
                            'price']
                        features['RATING'] = data['businesses'][i]['rating']
                        features['REVIEW_COUNT'] = data['businesses'][i]['review_count']
                        #features['IS_OPEN'] = 'Yes' if data['businesses'][i]['is_closed'] == False else 'No'
                        features['ADDRESS'] = ','.join(data['businesses'][i]['location']['display_address'])
                        features['PHONE'] = data['businesses'][i]['display_phone']
                        search_results.append(features)
                    df = utl_obj.create_table(search_results)


                    if len(df) != 0:
                        print(df)
                        df['CATEGORY'] = sub_menu[int(option)]
                        activity_choice1 = int(utl_obj.user_input('\nKindly enter the index of the place you would like to go:'))
                        selected_spot = df.iloc[activity_choice1 - 1]

                        recommendation = input("\nAre you happy with recommendation: Yes/No: ")
                        if activity_choice1:
                            if recommendation.upper() == "NO":
                                main()
                            if recommendation.upper() == "YES":
                                connect_db.insert_new_recommendation(int(usr.user_id), selected_spot)     ## Calling the function to insert activity choice to the database.
                                print("This recommendation will save to your favourites now!")
                            else:
                                print("Invalid selection")
                    else:
                        print('\nNo results found. Please modify your search')

                elif option == '0':                 # Return to Main menu
                    main()
                else:
                    print('Sorry, this is not a valid choice.')

            elif main_menu_option == '2':           # Customer support option from main menu
                print('\nHere are the customer support details:\n\nCustomer Support: 02036874453\nEmail Address:escapade@gmail.com\n\nTaking you back to main menu')

            elif main_menu_option == '0':           # Exit application option from main menu
                print('Thank you for using Escapade.\n')
                rating_exists = connect_db.check_rating_exists(usr.user_id)
                if rating_exists == False:
                    rating_option = utl_obj.user_input('Would you like to leave us a rating?Y/N: ')
                    if rating_option == 'Y':
                        app_rating = utl_obj.user_input('From 1-5,How would you rate us?')

                        connect_db.insert_application_rating(usr.user_id,app_rating)                   ## <Call the class method to insert application rating to DB.>
                        print('Thank you for rating us. It was a pleasure to serve you.')
                        Event().wait(3)
                        exit()
                    else:
                        Event().wait(3)
                        exit()
                else:
                    Event().wait(3)
                    exit()
            else:
                print('\nInvalid Selection')
    except Exception as e:
        print(e)
        print('Application Error. Please login again.')
        Event().wait(3)
        exit()


if __name__ == '__main__':
    main()
