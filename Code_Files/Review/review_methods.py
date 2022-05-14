from main import insert_record



def review_prompt():
    give_review= input('Would you like to leave a review for Buckingham Palace?:y/n ')
    if give_review=='y':
        user_review=input('leave your review: ')
        record = {
            'recommended_place': 'Buckingham Palace',
            'review': user_review,
        }
        insert_record(record)
    else:
        print('Thank you! Come back again!')

review_prompt()




